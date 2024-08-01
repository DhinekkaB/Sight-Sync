# Sight-Sync

## Introduction
The concept aims to revolutionize the mobility and independence of visually impaired individuals by integrating advanced technology into a user-friendly device.This innovative approach transforms how visually impaired people navigate their environment, enhancing their interaction and confidence.By merging cutting-edge solutions with practical design, the idea empowers users to experience greater autonomy in their daily lives.The end result is a groundbreaking device that significantly improves how visually impaired individuals perceive and move through their world.

## Idea Includes:
    1.Navigation
    2.Object Detection

### NAVIGATION
Visually-impaired people depend on others for navigation purpose. So this project helps them to navigate to places through voice input and destination is also given through voice command.
This code uses Google Maps API, speech recognition, and text-to-speech to provide navigational instructions. It captures the user's origin and destination via voice input using the SpeechRecognition library. These locations are then used to fetch directions from the Google Maps API. The instructions are cleaned to remove HTML tags and are spoken out loud using the pyttsx3 text-to-speech engine, guiding the user through the route step-by-step.

#### Dependencies
1. requests:
   ```
   pip install requests
   ```
   
2. pyttsx3:
   ```
   pip install pyttsx3
   ```
   
3. SpeechRecognition (speech_recognition):
   ```
   pip install SpeechRecognition
   ```
   
#### Technologies and Concepts
1. Google Maps API:
    The Google Maps API is used to get directions between two locations. The API returns detailed step-by-step instructions for the route.

2. Text-to-Speech (TTS):
    pyttsx3 is used to convert text instructions into spoken words. This allows users to hear navigation instructions.

3. Speech Recognition:
    SpeechRecognition library is used to capture and convert spoken words into text. This allows users to provide voice commands for their origin and destination.

### OBJECT DETECTION

This code snippet is for object detection using TensorFlow Lite and OpenCV. It starts by resizing the image frame and expanding its dimensions to match the model's input shape. If the model is floating-point, the image is normalized.The preprocessed image is fed into the TensorFlow Lite interpreter for inference. Results are extracted, including bounding box coordinates, class indices, and confidence scores. Detections with scores above a minimum threshold are processed, and bounding boxes are drawn on the original image.Detected objects are annotated with their class names and confidence percentages using OpenCV. The frame rate is also displayed. The processed frames are shown in a window named 'Object detector'. The loop runs until 'q' is pressed, after which the video stream stops and OpenCV windows close, ensuring a graceful shutdown.

#### Dependencies
1.TensorFlow Lite
   ```
   pip install tflite-runtime
   ```

2.OpenCV
   ```
   pip install opencv-python
   ```

3.NumPy
  ```
  pip install numpy
  ```

#### Technologies
1. Object Detection:
        Object detection involves identifying and locating objects within an image or video frame. This code uses a pre-trained TensorFlow Lite model to detect objects.
   
2. TensorFlow Lite Interpreter:
        The TensorFlow Lite interpreter runs the inference on the model with the input image data. The results include bounding boxes, class indices, and confidence scores.

3. Image Processing with OpenCV:
        OpenCV functions are used to resize images, draw bounding boxes, and display annotated frames. It also captures video from a webcam or a video file.

4. Normalization:
         Normalizing input data (subtracting the mean and dividing by the standard deviation) ensures the input data matches the scale of the data the model was trained on, improving detection accuracy.

5. Bounding Box Calculation and Annotation:
        The code calculates bounding box coordinates for detected objects, ensuring they stay within image boundaries. It then annotates the image with class labels and confidence scores.
