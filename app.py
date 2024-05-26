from flask import Flask, render_template, Response, jsonify
from music import start_music, stop_music_running, play_next_song, play_previous_song
from camera import *
import threading

app = Flask(__name__)

headings = ("Name", "Album", "Artist")
df1 = music_rec()
df1 = df1.head(15)

detected_emotion = None

# MUSIC_FOLDER = "static/music"

@app.route('/')
def index():
    print(df1.to_json(orient='records'))
    return render_template('index.html', headings=headings, data=df1)


def gen(camera):
    global detected_emotion
    global df1
    while True:
        frame, df1, detected_emotion = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/t')
def gen_table():
    return df1.to_json(orient='records')


@app.route('/play_music')
def play_music():
    if detected_emotion is not None:
        return start_music(detected_emotion)
    else:
        return "No emotion detected"


@app.route('/stop_music')
def stop_music():
    return stop_music_running()


@app.route('/next_song')
def next_song():
    play_next_song()
    return jsonify({"message": "Next song queued"})


@app.route('/previous_song')
def previous_song():
    play_previous_song()
    return jsonify({"message": "Next song queued"})


if __name__ == '__main__':
    app.debug = True
    app.run()
