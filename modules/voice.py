import pyttsx3
from modules.speech import listen

text = listen()

engine = pyttsx3.init()


def speak():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


speak()
