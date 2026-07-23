from core.speech import SpeechManager
from config import WAKE_WORD, EXIT_COMMANDS
from core.brain import Brain


class Assistant:

    def __init__(self, gui):

        self.gui = gui
        self.brain = Brain()
        self.speech = SpeechManager()

        self.wake_word = WAKE_WORD

    # --------------------------------------------

    def run(self):

        self.speech.speak("Krypton online, Boss.")

        self.gui.set_state("sleep")

        while True:

            self.gui.set_state("listen")

            text = self.speech.listen()

            if not text:
                continue

            text = text.strip().lower()

            if not text.startswith(self.wake_word):
                continue

            command = text.replace(
                self.wake_word,
                "",
                1
            ).strip()

            if not command:

                self.gui.set_state("happy")

                self.speech.speak(
                    "I'm listening, Boss."
                )

                self.conversation()

                continue

            self.process_command(command)

            self.conversation()

    # --------------------------------------------

    def conversation(self):

        while True:

            self.gui.set_state("listen")

            command = self.speech.listen()

            if not command:
                continue

            command = command.strip().lower()

            if any(
                word in command
                for word in EXIT_COMMANDS
            ):

                self.gui.set_state("sleep")

                self.speech.speak(
                    "Going back to sleep, Boss."
                )

                break

            self.process_command(command)

    # --------------------------------------------

    def process_command(self, command):

        self.gui.set_user(command)

        self.gui.set_state("think")

        response = self.brain.process(command)

        self.gui.set_assistant(response)

        self.gui.set_state("talk")

        self.speech.speak(response)