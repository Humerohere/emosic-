import os
import random
import pygame
from mutagen.mp3 import MP3

pygame.mixer.init()

# Define a custom event for when the music ends
MUSIC_END_EVENT = pygame.USEREVENT + 1

# Initialize global variables to keep track of the music files, the current index, and the current emotion
current_music_files = []
current_index = 0
current_emotion = None
previous_songs = []

def initialize_music():
    # Main event loop to handle music end events
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MUSIC_END_EVENT:
                play_next_song()

def start_music(emotion):
        try:

            global current_music_files, current_index, current_emotion, previous_songs
            current_emotion = emotion
            if emotion:
                music_folder = 'music_file'
                music_files = {
                    'Angry': os.listdir(os.path.join(music_folder, 'angry')),
                    'Disgusted': os.listdir(os.path.join(music_folder, 'disgusted')),
                    'Fearful': os.listdir(os.path.join(music_folder, 'fearful')),
                    'Happy': os.listdir(os.path.join(music_folder, 'happy')),
                    'Neutral': os.listdir(os.path.join(music_folder, 'neutral')),
                    'Sad': os.listdir(os.path.join(music_folder, 'sad')),
                    'Surprised': os.listdir(os.path.join(music_folder, 'surprised'))
                }
                music_file_list = music_files.get(emotion)
                if music_file_list:
                    current_music_files = music_file_list
                    current_index = 0

                    # Shuffle the music file list to randomize the order
                    random.shuffle(current_music_files)

                    # Load and play the first song
                    music_path = os.path.join(music_folder, emotion.lower(), current_music_files[current_index])
                    if os.path.exists(music_path):
                        pygame.mixer.music.load(music_path)
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_endevent(MUSIC_END_EVENT)
                        audio = MP3(music_path)
                        music_length = audio.info.length
                        print(f"Playing {emotion} music: {current_music_files[current_index]}")
                        return {"music_name": current_music_files[current_index], "music_length": music_length}
                    else:
                        print(f"Music file {current_music_files[current_index]} not found in the folder.")
                else:
                    print("No music found for the detected emotion.")
            return None
        except Exception as e:
            print("PLAYING MUSIC EXC: ",e)

def play_next_song():
    global current_index, current_emotion, previous_songs
    current_index += 1
    if current_index < len(current_music_files):
        music_path = os.path.join('music_file', current_emotion.lower(), current_music_files[current_index])
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(MUSIC_END_EVENT)
            previous_songs.append(current_music_files[current_index - 1])
            print(f"Playing next {current_emotion} music: {current_music_files[current_index]}")
    else:
        print("No more songs in the queue.")

def play_previous_song():
    global current_index, current_emotion, previous_songs
    if previous_songs:
        previous_song = previous_songs.pop()
        previous_index = current_music_files.index(previous_song)
        current_index = previous_index
        music_path = os.path.join('music_file', current_emotion.lower(), previous_song)
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(MUSIC_END_EVENT)
            print(f"Playing previous {current_emotion} music: {previous_song}")
    else:
        print("No previous songs in the history.")

def stop_music_running():
    pygame.mixer.music.stop()
