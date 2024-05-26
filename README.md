# Emotion-Music-Recommendation

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**Tech Stack**: Python, TensorFlow, Flask

Recommending music based on your facial expressions using the FER 2013 dataset and VGG19 model.

![emosic-web-animation (1)](https://github.com/Humerohere/emosic-/assets/124302121/de244a95-fd32-4a71-bb2d-14ccd7799be9)


## 🎵 Project Description

The emotion recognition model uses the VGG19 model trained on the FER 2013 dataset. It can detect 7 emotions. The project works by getting a live video feed from the webcam, passing it through the model to get a prediction of emotion. According to the predicted emotion, the app will fetch playlists of songs from music files, recommend the songs by displaying them on the screen, and play the music as well.

## ✨ Features

- Real-time expression detection and song recommendations.
- Playlists fetched from files and music can be played using the play-music-api.
- Skeumorphism UI for the website.

## 🚀 Running the App

### Flask

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python app.py
Run the application:
   python app.py
Give camera permission if asked.

## 🛠️ Tech Stack
TensorFlow
Keras
Spotipy
Tkinter (For testing)
Flask
scikit-learn
Pygame
pandas
numpy
Jupyter Notebook

## 📊 Dataset
The dataset used for this project is the FER2013 dataset. Models trained on this dataset can classify 7 emotions. The dataset can be found here.

## 🧠 Model Architecture
The model uses VGG19, a pre-trained Convolutional Neural Network:

VGG19 Backbone: The VGG19 model, pre-trained on ImageNet, is used without the top fully connected layers.
Global Average Pooling: Applied after the convolutional base.
Dense Layers: Additional Dense layers for classification:
Dense layer with 4096 units and ReLU activation with L2 regularization.
Output Dense layer with 7 units and softmax activation for classifying 7 emotions.
Training Setup:
Loss function: Categorical Crossentropy.
Optimizer: Adam with a learning rate of 0.0001.
Metrics: Accuracy.

## 🎓 Training
The images were normalized, resized to (48, 48), and converted to grayscale in batches of 64 using ImageDataGenerator in Keras. The training took around 20 minutes and was trained on Kaggle for 10 epochs, achieving an accuracy of approximately 80%.

## 🔧 Current Condition
The entire project works perfectly fine. Live detection provides good frame rates due to multithreading.

## 🛠️ Project Components
pygame: Module for establishing connection to and getting tracks from the music file using the pygame music.
haarcascade: For face detection.
camera.py: Module for video streaming, frame capturing, prediction, and recommendation, which are passed to main.py.
main.py: Main Flask application file.
index.html: Web page for the application located in the 'templates' directory. Basic HTML and CSS.
utils.py: Utility module for video streaming of the webcam with threads to enable real-time detection.
train.py: Script for image processing and training the model.






