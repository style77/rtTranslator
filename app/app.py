import queue
from threading import Thread
import tkinter as tk
from deep_translator import GoogleTranslator
import speech_recognition as sr

import pyaudiowpatch as pyaudio
from app.audio.stream import Speakers
from app.config import TARGET_LANGUAGE

from app.ui.window import Window


class App:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.4
    provider = recognizer.recognize_google
    translation_provider = GoogleTranslator(source='auto', target=TARGET_LANGUAGE).translate

    def __init__(self):
        self.audio_queue = queue.Queue()

        root = tk.Tk()
        self.window = Window(root)
        self.start_app_thread(root)

    @staticmethod
    def get_device():
        with pyaudio.PyAudio() as p:
            device = p.get_default_input_device_info()

        device_index = device["index"]
        sample_rate = int(device["defaultSampleRate"])

        return device_index, sample_rate

    def recognize_worker(self):
        while True:
            audio = (
                self.audio_queue.get()
            )
            if audio is None:
                break

            try:
                result = self.provider(audio, language=SOURCE_LANGUAGE)
                if not result:
                    continue

                translated_result = self.translation_provider(result)

                self.window.update_text(result, translated_result)

                print(f"Recognized: {result}")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results: {e}")

            self.audio_queue.task_done()

    def start_listening(self):
        recognize_thread = Thread(target=self.recognize_worker)
        recognize_thread.daemon = True
        recognize_thread.start()

        device_index, sample_rate = self.get_device()

        with Speakers(device_index=device_index, sample_rate=sample_rate) as source:
            try:
                while True:
                    self.audio_queue.put(self.recognizer.listen(source))
            except KeyboardInterrupt:
                pass

    def start_app_thread(self, root: tk.Tk):
        listening_thread = Thread(target=self.start_listening)
        listening_thread.daemon = True
        listening_thread.start()

        root.mainloop()
