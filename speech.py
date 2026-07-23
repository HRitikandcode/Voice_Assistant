from stt import WhisperSTT
from tts import PiperTTS




class SpeechManager:

    def __init__(self):
        self.stt = WhisperSTT()
        self.tts = PiperTTS()

    def listen(self):

        return self.stt.listen()

    def speak(self, text):

        self.tts.speak(text)