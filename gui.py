import customtkinter as ctk


class KryptonGUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("Krypton")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # ------------------------
        # Title
        # ------------------------

        self.title = ctk.CTkLabel(
            self.root,
            text="KRYPTON",
            font=("Consolas", 30, "bold")
        )

        self.title.pack(pady=20)

        # ------------------------
        # Face Canvas
        # ------------------------

        self.canvas = ctk.CTkCanvas(
            self.root,
            width=300,
            height=220,
            bg="#242424",
            highlightthickness=0
        )

        self.canvas.pack()

        # ------------------------
        # Status
        # ------------------------

        self.status = ctk.CTkLabel(
            self.root,
            text="Sleeping",
            font=("Arial", 18)
        )

        self.status.pack(pady=10)

        # ------------------------
        # User
        # ------------------------

        self.user = ctk.CTkLabel(
            self.root,
            text="👤 Boss : ---",
            wraplength=430,
            font=("Arial", 16)
        )

        self.user.pack(pady=15)

        # ------------------------
        # Assistant
        # ------------------------

        self.assistant = ctk.CTkLabel(
            self.root,
            text="🤖 Krypton : ---",
            wraplength=430,
            font=("Arial", 16)
        )

        self.assistant.pack()

        self.draw_sleep()

    # =====================================================
    # Drawing
    # =====================================================

    def clear_face(self):
        self.canvas.delete("all")

    def draw_sleep(self):

        self.clear_face()

        self.canvas.create_line(
            90, 80, 130, 80,
            width=6,
            fill="cyan"
        )

        self.canvas.create_line(
            170, 80, 210, 80,
            width=6,
            fill="cyan"
        )

        self.canvas.create_oval(
            145, 140, 155, 150,
            fill="cyan",
            outline="cyan"
        )

    def draw_listening(self):

        self.clear_face()

        self.canvas.create_oval(
            90, 60, 130, 100,
            outline="cyan",
            width=4
        )

        self.canvas.create_oval(
            170, 60, 210, 100,
            outline="cyan",
            width=4
        )

        self.canvas.create_line(
            140, 150,
            160, 150,
            fill="cyan",
            width=4
        )

    def draw_thinking(self):

        self.clear_face()

        self.canvas.create_oval(
            90, 60, 130, 100,
            fill="cyan",
            outline="cyan"
        )

        self.canvas.create_oval(
            170, 60, 210, 100,
            fill="cyan",
            outline="cyan"
        )

        self.canvas.create_oval(
            145, 140, 155, 150,
            fill="cyan",
            outline="cyan"
        )

    def draw_talking(self):

        self.clear_face()

        self.canvas.create_oval(
            90, 60, 130, 100,
            outline="cyan",
            width=4
        )

        self.canvas.create_oval(
            170, 60, 210, 100,
            outline="cyan",
            width=4
        )

        self.canvas.create_oval(
            140, 135, 160, 165,
            outline="cyan",
            width=4
        )

    def draw_happy(self):

        self.clear_face()

        self.canvas.create_arc(
            90, 60, 130, 90,
            start=0,
            extent=180,
            style="arc",
            outline="cyan",
            width=4
        )

        self.canvas.create_arc(
            170, 60, 210, 90,
            start=0,
            extent=180,
            style="arc",
            outline="cyan",
            width=4
        )

        self.canvas.create_arc(
            110, 110, 190, 180,
            start=180,
            extent=180,
            style="arc",
            outline="cyan",
            width=4
        )

    # =====================================================
    # Thread-safe Updates
    # =====================================================

    def _update_state(self, state):

        if state == "sleep":
            self.draw_sleep()
            self.status.configure(text="Sleeping")

        elif state == "listen":
            self.draw_listening()
            self.status.configure(text="Listening...")

        elif state == "think":
            self.draw_thinking()
            self.status.configure(text="Thinking...")

        elif state == "talk":
            self.draw_talking()
            self.status.configure(text="Speaking...")

        elif state == "happy":
            self.draw_happy()
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

    # =====================================================

    def run(self):
        self.root.mainloop()