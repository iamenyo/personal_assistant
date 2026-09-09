<<<<<<< HEAD
English | [Français](README.fr.md)

# Lumin

Lumin is a personal voice assistant built in Python for Windows. It listens for voice commands and executes actions: telling the date, opening or closing applications, opening websites, and soon much more thanks to the planned Gemini API integration.

This project is developed solo, mainly for my personal use and to learn. Feel free to check the Contributing section below if you'd like to help.

## Current features

- Voice recognition (French) via Google Speech Recognition
- Text-to-speech via pyttsx3
- Tell today's date
- Open installed applications (Discord, Edge, VS Code, Epic Games...)
- Close applications
- Open websites (YouTube, Google, GitHub...)

## Coming soon

- Gemini API integration for natural language understanding, beyond keyword matching
- Offline voice recognition (Vosk)
- More commands (weather, search, timer, voice notes...)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lumin.git
   cd lumin
   ```

2. Install dependencies:
=======
# Lumin

Lumin est un assistant personnel vocal développé en Python pour Windows. Il écoute des commandes vocales et exécute des actions : donner la date, ouvrir ou fermer des applications, ouvrir des sites web, et bientôt bien plus grâce à l'intégration prévue de l'API Gemini.

Ce projet est développé en solo, avant tout pour mon usage personnel et pour apprendre. N'hésitez pas à consulter la section Contribution plus bas si vous voulez aider.

## Fonctionnalités actuelles

- Reconnaissance vocale (français) via Google Speech Recognition
- Synthèse vocale via pyttsx3
- Donner la date du jour
- Ouvrir des applications installées (Discord, Edge, VS Code, Epic Games...)
- Fermer des applications
- Ouvrir des sites web (YouTube, Google, GitHub...)

## À venir

- Intégration de l'API Gemini pour comprendre le langage naturel, au-delà des mots-clés
- Reconnaissance vocale hors-ligne (Vosk)
- D'autres commandes (météo, recherche, minuteur, notes vocales...)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/ton-username/lumin.git
   cd lumin
   ```

2. Installez les dépendances :
>>>>>>> 0dcd5a7a5dc2a36a4d7169c5649105a1a97a5f99
   ```bash
   pip install -r requirements.txt
   ```

<<<<<<< HEAD
   Note: PyAudio can sometimes fail to install directly on Windows. If that happens:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

3. Adjust the application paths in `modules/apps.py` to match your own installation (paths can vary between machines).

4. Run the assistant:
=======
3. Adaptez les chemins des applications dans `modules/apps.py` selon votre installation (les chemins peuvent varier selon les machines).

4. Lancez l'assistant :
>>>>>>> 0dcd5a7a5dc2a36a4d7169c5649105a1a97a5f99
   ```bash
   python main.py
   ```

<<<<<<< HEAD
## Project structure

```
Lumin/
├── main.py              Entry point, main loop
├── modules/
│   ├── speech.py         Listening and voice recognition
│   ├── voice.py          Text-to-speech
│   ├── commands.py       Decision logic (keywords to actions)
│   ├── apps.py            Open or close local applications
│   └── web.py              Open websites
└── README.md
```

## Example voice commands

| You say                 | Lumin does                          |

| "What day is it?"       | Announces today's date               |
| "Open Discord"          | Launches Discord                     |
| "Close Discord"         | Closes Discord                       |
| "Open YouTube"          | Opens YouTube in the browser         |

## Contributing

This is primarily a personal learning project. I prefer to write the code myself to keep learning, so rather than pull requests that modify the code directly, I'm very open to feedback, suggestions, and bug reports.

If you see something that could be improved, please open an issue explaining what could be better and why. This helps me learn while keeping control over my own code.

## Notes

- The project is currently based on a keyword-matching system, not generative AI yet. Gemini integration is planned for more natural command understanding.
- Tested on Windows only.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
=======
## Structure du projet

```
Lumin/
├── main.py              Point d'entrée, boucle principale
├── modules/
│   ├── speech.py         Écoute et reconnaissance vocale
│   ├── voice.py          Synthèse vocale (texte vers voix)
│   ├── commands.py       Logique de décision (mots-clés vers actions)
│   ├── apps.py            Ouvrir ou fermer des applications locales
│   └── web.py              Ouvrir des sites web
└── README.md
```

## Exemples de commandes vocales

| Vous dites             | Lumin fait                        |

| "Quel jour on est ?"   | Annonce la date du jour            |
| "Ouvre Discord"        | Lance l'application Discord        |
| "Ferme Discord"        | Ferme l'application Discord        |
| "Ouvre YouTube"        | Ouvre YouTube dans le navigateur   |

## Contribution

Ce projet est avant tout un projet d'apprentissage personnel. Je préfère écrire le code moi-même pour progresser, donc plutôt que des pull requests qui modifient directement le code, je suis très preneur de retours, suggestions, et signalements de bugs.

Si vous voyez quelque chose à améliorer, ouvrez une issue en expliquant ce qui pourrait être mieux fait et pourquoi. Ça m'aide à apprendre tout en gardant le contrôle sur mon propre code.

## Notes

- Projet actuellement basé sur un système de mots-clés, pas encore d'IA générative. L'intégration de Gemini est prévue pour une compréhension plus naturelle des commandes.
- Testé sur Windows uniquement.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
>>>>>>> 0dcd5a7a5dc2a36a4d7169c5649105a1a97a5f99
