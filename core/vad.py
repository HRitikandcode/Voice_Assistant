from silero_vad import load_silero_vad, get_speech_timestamps
import sounddevice as sd
import numpy as np


class VoiceActivityDetector:

    def __init__(self):

        print("Loading VAD...")

        self.model = load_silero_vad()

        self.sample_rate = 16000

        print("VAD Ready!")

    def detect(self, duration=0.5):

        """
        Listen for a short time and
        return True if speech is detected.
        """

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        audio = np.squeeze(audio)

        timestamps = get_speech_timestamps(
            audio,
            self.model,
            sampling_rate=self.sample_rate
        )

        return len(timestamps) > 0