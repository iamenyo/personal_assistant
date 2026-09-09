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
   ```bash
   pip install -r requirements.txt
   ```

   Note: PyAudio can sometimes fail to install directly on Windows. If that happens:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

3. Adjust the application paths in `modules/apps.py` to match your own installation (paths can vary between machines).

4. Run the assistant:
   ```bash
   python main.py
   ```

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
