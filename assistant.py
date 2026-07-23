from speech import SpeechManager
from config import WAKE_WORD, EXIT_COMMANDS
from brain import Brain


class Assistant:

    def __init__(self):
        self.brain = Brain()
        self.speech = SpeechManager()
        self.wake_word = WAKE_WORD

    def run(self):
        self.speech.speak("Assistant started.")

        while True:
            text = self.speech.listen()

            if not text:
                continue

            text = text.strip().lower()

            if text.startswith(self.wake_word):

                # Remove wake word
                command = text.replace(self.wake_word, "", 1).strip()

                # If user only said the wake word
                if not command:
                    self.speech.speak("Hello Boss! How can I help you?")
                    self.conversation()
                    continue

                # User already gave a command
                response = self.brain.process(command)
                self.speech.speak(response)

                # Stay in conversation mode
                self.conversation()

    def conversation(self):

        while True:

            command = self.speech.listen()

            if not command:
                continue

            command = command.strip().lower()

            # Exit conversation
            if any(exit_cmd in command for exit_cmd in EXIT_COMMANDS):
                self.speech.speak("Okay. Going back to sleep.")
                break

            response = self.brain.process(command)

            self.speech.speak(response)