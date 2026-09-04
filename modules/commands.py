from datetime import datetime
from modules.voice import speak
from modules.apps import open_app, close_app


def tell_date(text):
    today = datetime.now().strftime("%A %d %B %Y")
    speak(f"Nous sommes le {today}")


def open_app_command(text):
    for trigger in ["ouvre", "lance", "open", "start"]:
        if trigger in text:
            app_name = text.replace(trigger, "").strip()
            break
    else:
        app_name = text

    if open_app(app_name):
        speak(f"Ouverture de {app_name}")
    else:
        speak("Je ne connais pas cette application")


def close_app_command(text):
    for trigger in ["ferme", "quitte", "close", "exit"]:
        if trigger in text:
            app_name = text.replace(trigger, "").strip()
            break
    else:
        app_name = text

    if close_app(app_name):
        speak(f"Fermeture de {app_name}")
    else:
        speak("Je ne connais pas cette application")


COMMANDS = [
    {
        "keywords": ["date", "quel jour", "on est quel jour"],
        "action": tell_date
    },
    {
        "keywords": ["ouvre", "lance", "open", "start"],
        "action": open_app_command
    },
    {
        "keywords": ["ferme", "quitte", "close", "exit"],
        "action": close_app_command
    }
]


def execute(text):
    text = text.lower()
    for command in COMMANDS:
        if any(keyword in text for keyword in command["keywords"]):
            command["action"](text)
            return True
    speak("Je n'ai pas compris la commande")
    return False
