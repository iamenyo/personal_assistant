import pyttsx3
from modules.speech import listen

engine = pyttsx3.init()


def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
