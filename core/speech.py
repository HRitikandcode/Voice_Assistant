from core.stt import WhisperSTT
from core.tts import PiperTTS
from core.vad import VoiceActivityDetector

import threading
import time


class SpeechManager:

    def __init__(self):

        self.stt = WhisperSTT()
        self.tts = PiperTTS()
        self.vad = VoiceActivityDetector()

        self.interrupted = False

    # --------------------------------------------------

    def listen(self):
        return self.stt.listen()

    # --------------------------------------------------

    def speak(self, text):

        self.interrupted = False

        interrupt_thread = threading.Thread(
            target=self._interrupt_listener,
            daemon=True
        )

        interrupt_thread.start()

        self.tts.speak(text)

    # --------------------------------------------------

    def stop(self):

        self.interrupted = True
        self.tts.stop()

    # --------------------------------------------------

    def is_speaking(self):

        return self.tts.is_speaking

    # --------------------------------------------------

    def _interrupt_listener(self):

        while self.tts.is_speaking:

            try:

                if self.vad.detect():

                    print("\nVoice detected. Interrupting Krypton...")

                    self.stop()

                    return

            except Exception as e:

                print("VAD Error:", e)

            time.sleep(0.05)