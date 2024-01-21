import os
import tkinter as tk
from typing import Any

from infi.systray import SysTrayIcon


class TrayIcon:
    def __init__(self):
        menu_options = ()

        path_icon = r"logo.ico"

        default_stop_callback = lambda _: os._exit(0)  # noqa

        systray = SysTrayIcon(
            path_icon,
            "rtTranslator",
            menu_options,
            on_quit=default_stop_callback,
        )
        systray.start()


class Window:
    def __init__(self, root: tk.Tk):
        self.root = root

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        self.root.overrideredirect(True)

        self.root.geometry(f"{width}x{height}")

        self.root.configure(bg="white")

        self.root.lift()

        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "white")

        self.main_text = tk.Label(
            text="",
            font=("Helvetica", "22"),
            fg="#eee",
            bg="white",
            wraplength=width - 300,
            justify="center",
        )
        self.sub_text = tk.Label(
            text="Waiting for recognizer",
            font=("Helvetica", "14"),
            fg="#ddd",
            bg="white",
            wraplength=width - 300,
            justify="center",
        )

        self.sub_text.pack(side="bottom", fill="both", pady=(0, 24))
        self.main_text.pack(side="bottom", fill="both")

    def update_text(self, text: str, translation_provider: Any):
        self.sub_text.configure(text=text)
        self.sub_text.update()

        self.main_text.configure(text=translation_provider(text))
        self.main_text.update()

    def setup_tray_icon(self):
        TrayIcon()

    def close_window(self):
        self.root.destroy()
