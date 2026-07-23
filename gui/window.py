import customtkinter as ctk

from gui.face import Face
from gui.animation import Animator
from gui.theme import *


class KryptonGUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("Krypton")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(fg_color=BACKGROUND)

        # ===========================
        # Title
        # ===========================

        self.title = ctk.CTkLabel(
            self.root,
            text="KRYPTON",
            font=TITLE_FONT,
            text_color=CORE
        )

        self.title.pack(pady=(20, 10))

        # ===========================
        # Canvas
        # ===========================

        self.canvas = ctk.CTkCanvas(
            self.root,
            width=WINDOW_WIDTH,
            height=420,
            bg=BACKGROUND,
            highlightthickness=0
        )

        self.canvas.pack()

        # ===========================
        # Face
        # ===========================

        self.face = Face(self.canvas)

        # ===========================
        # Animator
        # ===========================

        self.animator = Animator(
            self.root,
            self.face
        )

        self.animator.start()

        # ===========================
        # Status
        # ===========================

        self.status = ctk.CTkLabel(
            self.root,
            text="Sleeping",
            font=STATUS_FONT,
            text_color=CORE
        )

        self.status.pack(pady=(15, 10))

        # ===========================
        # User
        # ===========================

        self.user = ctk.CTkLabel(
            self.root,
            text="👤 Boss : ---",
            font=TEXT_FONT,
            wraplength=650,
            justify="center",
            text_color=TEXT
        )

        self.user.pack(pady=8)

        # ===========================
        # Assistant
        # ===========================

        self.assistant = ctk.CTkLabel(
            self.root,
            text="🤖 Krypton : ---",
            font=TEXT_FONT,
            wraplength=650,
            justify="center",
            text_color=TEXT
        )

        self.assistant.pack(pady=8)

    # ===================================================
    # Thread-safe GUI updates
    # ===================================================

    def _update_state(self, state):

        self.animator.set_mode(state)

        if state == "sleep":
            self.status.configure(text="Sleeping")

        elif state == "listen":
            self.status.configure(text="Listening...")

        elif state == "think":
            self.status.configure(text="Thinking...")

        elif state == "talk":
            self.status.configure(text="Speaking...")

        elif state == "happy":
            self.status.configure(text="Ready")

    def set_state(self, state):

        self.root.after(
            0,
            lambda: self._update_state(state)
        )

    def set_user(self, text):

        self.root.after(
            0,
            lambda: self.user.configure(
                text=f"👤 Boss : {text}"
            )
        )

    def set_assistant(self, text):

        self.root.after(
            0,
            lambda: self.assistant.configure(
                text=f"🤖 Krypton : {text}"
            )
        )

    # ===================================================

    def run(self):

        self.root.mainloop()