from stt import WhisperSTT

stt = WhisperSTT()

while True:
    text = stt.listen()
    print(text)