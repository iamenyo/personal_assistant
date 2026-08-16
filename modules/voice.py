import pyttsx3


engine = pyttsx3.init()


def speak():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hi Enk! what can i do for you")
    engine.runAndWait()

