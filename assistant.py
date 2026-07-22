from speech import SpeechManager
from commands import execute
from ai import ask
from config import WAKE_WORD, EXIT_COMMANDS


class Assistant:

    def __init__(self):
        self.speech = SpeechManager()
        self.wake_word = WAKE_WORD

    def run(self):
        self.speech.speak("Assistant started.")

        while True:
            text = self.speech.listen()

            if not text:
                continue

            if self.wake_word in text:
                self.speech.speak("Hello Boss! How can I help you?")
                self.conversation()

    def conversation(self):
        
        while True:
            command = self.speech.listen()

            if not command:
                continue

            # Exit conversation
            if any(word in command for word in EXIT_COMMANDS):
                self.speech.speak("Okay. Going back to sleep.")
                break

            # Try local commands first
            response = execute(command)

            # If no local command matches, ask the AI
            if response is None:
                response = ask(command)

            # Speak the response
            self.speech.speak(response)