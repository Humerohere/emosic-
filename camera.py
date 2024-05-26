import numpy as np
import cv2
import requests
from PIL import Image
from keras import Model
from keras.applications import VGG19
from keras.layers import Dense,GlobalAveragePooling2D
from keras.regularizers import l2
from threading import Thread
import pandas as pd
import pygame

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
ds_factor = 0.6
vgg19_model = VGG19(include_top=False, input_shape=(48, 48, 3))

for layer in vgg19_model.layers[-4:]:
    layer.trainable = True

x = GlobalAveragePooling2D()(vgg19_model.output)
x = Dense(1024, activation='relu', kernel_regularizer=l2(0.01))(x)
predictions = Dense(7, activation='softmax')(x)

emotion_model = Model(inputs=vgg19_model.input, outputs=predictions)

file_path = 'weights/vgg19_model.h5'
emotion_model.load_weights(file_path)


cv2.ocl.setUseOpenCL(False)

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
music_dist = {0: "songs/angry.csv", 1: "songs/disgusted.csv ", 2: "songs/fearful.csv", 3: "songs/happy.csv",
              4: "songs/neutral.csv", 5: "songs/sad.csv", 6: "songs/surprised.csv"}
global last_frame1
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
global cap1
show_text = [0]

class WebcamVideoStream:

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return
            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True


''' Class for reading video stream, generating prediction and recommendations '''


class VideoCamera(object):

    def get_frame(self):
        global cap1
        global df1
        cap1 = WebcamVideoStream(src=0).start()
        image = cap1.read()
        image = cv2.resize(image, (600, 500))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        df1 = pd.read_csv(music_dist[show_text[0]])
        df1 = df1[['Name', 'Album', 'Artist']]
        df1 = df1.head(15)
        detected_emotion = "Unknown"
        for (x, y, w, h) in face_rects:
            cv2.rectangle(image, (x, y - 50), (x + w, y + h + 10), (0, 255, 0), 2)
            roi_gray_frame = gray[y:y + h, x:x + w]
            cropped_img = cv2.cvtColor(roi_gray_frame, cv2.COLOR_GRAY2RGB)
            cropped_img = np.expand_dims(cv2.resize(cropped_img, (48, 48)), axis=0)
            prediction = emotion_model.predict(cropped_img)

            maxindex = int(np.argmax(prediction))
            show_text[0] = maxindex
            detected_emotion = emotion_dict[maxindex]
            cv2.putText(image, detected_emotion, (x + 20, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                        2, cv2.LINE_AA)
            df1 = music_rec()
        global last_frame1
        last_frame1 = image.copy()
        pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(last_frame1)
        img = np.array(img)
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes(), df1, detected_emotion


def music_rec():
    df = pd.read_csv(music_dist[show_text[0]])
    df = df[['Name', 'Album', 'Artist']]
    df = df.head(15)
    return df
