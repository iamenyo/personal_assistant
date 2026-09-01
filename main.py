from modules.speech import listen
from modules.commands import execute
from modules.voice import speak


def main():
    speak("Assistant ready")
    while True:
        try:
            text = listen()
            print(f"Heard: {text}")
            execute(text)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
