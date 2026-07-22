from speech import SpeechManager

speech = SpeechManager()

while True:

    text = speech.listen()

    if text:
        speech.speak(f"You said {text}")