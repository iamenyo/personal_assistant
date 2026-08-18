import speech_recognition as sr


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("say something...")
        audio_text = r.listen(source)
        print("Working")

    text = r.recognize_google(audio_text)
    return text
