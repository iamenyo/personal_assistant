from datetime import datetime
from modules.voice import speak
from modules.apps import open_app, close_app
from modules.web import open_website


def tell_date(text):
    today = datetime.now().strftime("%A %d %B %Y")
    speak(f"Nous sommes le {today}")


def open_app_command(text):
    for trigger in ["ouvre", "lance", "allume"]:
        if trigger in text:
            name = text.replace(trigger, "").strip()
            break
        else:
            name = text

    if open_app(name):
        speak(f"Ouverture de {name}")
    elif open_website(name):
        speak(f"Ouverture de {name}")
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
    },
    {
        "keywords": ["ouvre", "visite", "open website", "open site", "go to", "navigate to", "open"],
        "action": open_app_command
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
