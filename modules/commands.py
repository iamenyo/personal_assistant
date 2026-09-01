from datetime import datetime
from modules.voice import speak


def donner_date():
    ajourdhui = datetime.now().strftime("%A %d %B %Y")
    speak(f"Nous sommes le {aujourdhui}")


def activer_game_mode():
    speak("Activation du mode jeux")

COMMANDS = [
    {
        "keywords": ["date", "quel jour", "on est quel jour", "quelle date", "quelle est la date"],
        "action": donner_date
    },
    {
        "keywords": ["game mode", "mode jeux", "activer le mode jeux", "activer le mode game", "active le mode gaming"],
        "action": activer_game_mode
    },
]
