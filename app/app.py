import queue
import os
from threading import Thread
import tkinter as tk
from deep_translator import GoogleTranslator
import speech_recognition as sr

import pyaudiowpatch as pyaudio
from config import Config
from audio.stream import Speakers

from ui.window import Window


class App:
    config = Config(os.environ.get("CONFIG_PATH", "config.json"))
    recognizer = sr.Recognizer()
    provider = recognizer.recognize_google
    translation_provider = GoogleTranslator(
        source="auto", target=config.target_language
    ).translate

    def __init__(self):
        self.audio_queue = queue.Queue()

        self.root = root = tk.Tk()
        self.window = Window(root)
        self.start_app_thread()

    @staticmethod
    def get_device():
        with pyaudio.PyAudio() as p:
            device = p.get_default_input_device_info()

        device_index = device["index"]
        sample_rate = int(device["defaultSampleRate"])

        return device_index, sample_rate

    def recognize_worker(self):
        while True:
            audio = self.audio_queue.get()
            if audio is None:
                break

            try:
                result = self.provider(audio, language=self.config.source_language(self))
                if not result:
                    continue

                self.window.update_text(result, self.translation_provider)

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

    def start_app_thread(self):
        listening_thread = Thread(target=self.start_listening)
        listening_thread.daemon = True
        listening_thread.start()

        self.window.setup_tray_icon()

        self.root.mainloop()
