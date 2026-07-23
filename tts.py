from piper import PiperVoice
import sounddevice as sd
import numpy as np


class PiperTTS:

    def __init__(self):
        self.voice = PiperVoice.load(
            "models/en_US-kristin-medium.onnx"
        )

    def speak(self, text):

        if not text:
            return

        # Add a tiny pause at the end
        text = text.strip() + "  "

        print(f"Vector: {text}")

        chunks = []
        sample_rate = None

        for chunk in self.voice.synthesize(text):
            chunks.append(chunk.audio_int16_array)
            sample_rate = chunk.sample_rate

        if not chunks:
            return

        audio = np.concatenate(chunks)

        audio = audio.astype("float32") / 32768.0

        sd.stop()
        sd.play(audio, samplerate=sample_rate)
        sd.wait()