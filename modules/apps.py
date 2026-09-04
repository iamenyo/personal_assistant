import os
import subprocess

APP_PATHS = [
    {
        "names": ["discord","discorde"],
        "path": os.path.expandvars(r"%LOCALAPPDATA%\Discord\Update.exe"),
        "process": "Discord.exe"
    },
    {
        "names": ["edge"],
        "path": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "process": "msedge.exe"
    },
    {
        "names": ["vscode", "visual studio code"],
        "path": os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"),
        "process": "Code.exe"
    },
    {
        "names": ["epic", "epic games"],
        "path": r"C:\Program Files\Epic Games\Launcher\Binaries\Win32\EpicGamesLauncher.exe",
        "process": "EpicGamesLauncher.exe"
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


def close_app(app_name):
    app_name = app_name.lower()
    for app in APP_PATHS:
        if app_name in app["names"]:
            subprocess.run(["taskkill", "/F", "/IM", app["process"]], capture_output=True)
            return True
    return False

