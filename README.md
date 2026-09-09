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
   ```bash
   pip install -r requirements.txt
   ```

3. Adaptez les chemins des applications dans `modules/apps.py` selon votre installation (les chemins peuvent varier selon les machines).

4. Lancez l'assistant :
   ```bash
   python main.py
   ```

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
