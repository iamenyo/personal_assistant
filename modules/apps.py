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


def open_app(app_name):
    app_name = app_name.lower()
    for app in APP_PATHS:
        if app_name in app["names"]:
            if app["names"][0] == "discord":
                os.startfile(app["path"], arguments="--processStart Discord.exe")
            else:
                os.startfile(app["path"])
            return True
    return False
