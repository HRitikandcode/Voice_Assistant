from piper import PiperVoice
import sounddevice as sd
import numpy as np
import re


class PiperTTS:

    def __init__(self):

        self.voice = PiperVoice.load(
            "models/en_US-kristin-medium.onnx"
        )

        self.is_speaking = False
        self.stop_requested = False

    # --------------------------------------------------

    def clean_text(self, text):

        text = re.sub(r'#+\s*', '', text)
        text = re.sub(r'[*_`]', '', text)
        text = re.sub(r'>\s*', '', text)
        text = re.sub(r'^\s*[-•]\s*', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\d+\.\s*', '', text, flags=re.MULTILINE)
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', text)
        text = re.sub(r'https?://\S+', '', text)

        text = text.replace("\n", ". ")

        text = re.sub(r'\.{2,}', '.', text)
        text = re.sub(r'\!{2,}', '!', text)
        text = re.sub(r'\?{2,}', '?', text)

        text = re.sub(r'\s+', ' ', text)

        return text.strip()

    # --------------------------------------------------

    def stop(self):

        self.stop_requested = True
        self.is_speaking = False

        sd.stop()

    # --------------------------------------------------

    def speak(self, text):

        if not text:
            return

        text = self.clean_text(text)

        print(f"Krypton: {text}")

        self.stop_requested = False
        self.is_speaking = True

        for chunk in self.voice.synthesize(text):

            if self.stop_requested:
                break

            audio = chunk.audio_int16_array.astype(np.float32)
            audio /= 32768.0

            sd.play(audio, samplerate=chunk.sample_rate)

            sd.wait()

            if self.stop_requested:
                break

        sd.stop()

        self.is_speaking = False