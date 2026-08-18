import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something...")
    audio_text = r.listen(source)
    print("Working")

try:
    print("Text :" + r.recognize_google(audio_text))
except sr.UnknownValueError:
    print("I don't understand the audio")
