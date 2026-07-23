from faster_whisper import WhisperModel
import speech_recognition as sr
import tempfile
import os


class WhisperSTT:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

        self.recognizer = sr.Recognizer()

        # Better recognition settings
        self.recognizer.energy_threshold = 250
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 1.2
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.6

        print("Calibrating microphone...")

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=2
            )

        print("Whisper Ready!")

    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=15
                )

            except sr.WaitTimeoutError:
                return ""

            except Exception:
                return ""

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp:

            wav_path = temp.name

        with open(wav_path, "wb") as f:
            f.write(audio.get_wav_data())

        try:

            segments, info = self.model.transcribe(
                wav_path,
                language="en",
                beam_size=3,
                vad_filter=True,
                condition_on_previous_text=False,
                temperature=0
            )

            text = " ".join(
                segment.text.strip()
                for segment in segments
            ).strip().lower()

        finally:

            if os.path.exists(wav_path):
                os.remove(wav_path)

        if text:
            print(f"User: {text}")

        return text