import requests
import pyttsx3
import speech_recognition as sr
import re

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to get directions from Google Maps API
def get_directions(api_key, origin, destination):
    # base_url = 
    params = {
        "origin": origin,
        "destination": destination,
        "key": api_key
    }
    
    response = requests.get(base_url, params=params)
    directions = response.json()
    
    if directions['status'] == 'OK':
        steps = directions['routes'][0]['legs'][0]['steps']
        return steps
    else:
        print("Error:", directions['status'])
        return None

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert it to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("I could not understand your voice. Please try again.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            speak("There was an error with the speech recognition service. Please try again.")
            return None

# Main function
def main():
    # Replace with your Google Maps API key
    # api_key = add api_key
    
    print("Starting the navigation script.")
    
    speak("Please say the starting location.")
    origin = recognize_speech()
    if origin is None:
        return
    
    speak("Please say the destination.")
    destination = recognize_speech()
    if destination is None:
        return
    
    steps = get_directions(api_key, origin, destination)
    
    if steps:
        for i, step in enumerate(steps):
            instruction = step['html_instructions']
            # Remove HTML tags from instruction
            instruction = re.sub(r'<.*?>', '', instruction)
            print(f"Step {i+1}: {instruction}")
            speak(f"Step {i+1}: {instruction}")
    else:
        print("No steps found.")

if _name_ == "_main_":
    main()