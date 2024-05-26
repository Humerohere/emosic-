
# Emosic: Emotion-Powered Music Recommendation

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## 🎵 Project Overview

Emosic is an emotion-powered music recommendation system. It utilizes a facial expression recognition model based on the VGG19 architecture trained on the FER 2013 dataset to detect emotions in real-time from live video feed. Based on the detected emotions, Emosic recommends personalized playlists and seamlessly plays the recommended music.

![Emosic Demo](https://github.com/Humerohere/emosic-/assets/124302121/de244a95-fd32-4a71-bb2d-14ccd7799be9)

## ✨ Key Features

- **Real-time Expression Detection:** Analyzes facial expressions in real-time to determine emotional state.
- **Dynamic Playlist Generation:** Recommends playlists based on detected emotions for a personalized music experience.
- **Seamless Music Playback:** Integrates with the play-music-api for seamless playback of recommended tracks.
- **Intuitive User Interface:** Boasts a skeuomorphic UI design for enhanced user interaction and immersion.

## 🚀 Running the App

### Flask

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```
   Give camera permission if asked.

## 🛠️ Tech Stack

- TensorFlow
- Keras
- Flask
- scikit-learn
- Pygame
- pandas
- numpy
- Jupyter Notebook
- openCV

## 🧠📊 Dataset and Architecture Overview

The dataset used for this project is the FER2013 dataset, containing facial expressions classified into 7 emotions.

### VGG19 Backbone:

- The VGG19 model, pre-trained on ImageNet, is used without the top fully connected layers.
- Global Average Pooling is applied after the convolutional base.
- Additional Dense layers are added for classification.

## Training Setup:

- **Loss function:** Categorical Crossentropy.
- **Optimizer:** Adam with a learning rate of 0.0001.
- **Metrics:** Accuracy.

## 🎓 Training Process

Images were preprocessed, normalized, resized to (48, 48), and converted to grayscale in batches of 64 using ImageDataGenerator in Keras. The training took around 20 minutes on Kaggle for 10 epochs, achieving an accuracy of approximately 80%.

## 🔧 Project Status

The entire project works perfectly fine. Live detection provides good frame rates due to multithreading.

## 🛠️ Important Components

- **pygame:** Module for establishing connection to and getting tracks from the music file using the pygame music.
- **haarcascade:** For face detection.
- **camera.py:** Module for video streaming, frame capturing, prediction, and recommendation.
- **main.py:** Main Flask application file.
- **index.html:** Web page for the application located in the 'templates' directory. Basic HTML and CSS.
- **utils.py:** Utility module for video streaming of the webcam with threads to enable real-time detection.
- **train.py:** Script for image processing and training the model.
