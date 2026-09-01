import os

APP_PATHS = [
    {
        "names": ["discord"],
        "path": os.path.expandvars(r"%LOCALAPPDATA%\Discord\Update.exe")
    },
    {
        "names": ["edge"],
        "path": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    },
    {
        "names": ["vscode", "visual studio code"],
        "path": os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe")
    },
    {
        "names": ["epic", "epic games"],
        "path": r"C:\Program Files\Epic Games\Launcher\Binaries\Win32\EpicGamesLauncher.exe"
    }
]
