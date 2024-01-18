import tkinter as tk


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
        )
        self.sub_text = tk.Label(
            text="Waiting for recognizer",
            font=("Helvetica", "14"),
            fg="#ddd",
            bg="white",
        )

        self.sub_text.pack(side="bottom", fill="both", pady=(0, 24))
        self.main_text.pack(side="bottom", fill="both")

    def update_text(self, text: str, translated_text: str):
        self.sub_text.configure(text=text)
        self.main_text.configure(text=translated_text)

        self.sub_text.update()
        self.main_text.update()
