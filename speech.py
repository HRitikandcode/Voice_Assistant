import speech_recognition as sr
import pyttsx3


class SpeechManager:
    def __init__(self):
        # Speech Recognition
        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8

        # Text To Speech
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 175)

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[0].id)

        print("Calibrating microphone...")

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)

        print("Microphone Ready!")

    def speak(self, text):
        print(f"Assistant: {text}")

        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

                text = self.recognizer.recognize_google(audio)

                print(f"User: {text}")

                return text.lower()

            except sr.WaitTimeoutError:
                return ""

            except sr.UnknownValueError:
                return ""

            except sr.RequestError:
                self.speak("I'm unable to connect to speech recognition.")
                return ""

            except Exception as e:
                print(e)
                return ""