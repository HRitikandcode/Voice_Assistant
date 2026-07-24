import subprocess
import os


def open_chrome():

    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for path in paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return "Opening Chrome, Boss."

    return "Chrome is not installed."


def open_vscode():

    paths = [
        r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        r"C:\Program Files\Microsoft VS Code\Code.exe"
    ]

    for path in paths:

        path = os.path.expandvars(path)

        if os.path.exists(path):
            subprocess.Popen(path)
            return "Opening VS Code."

    return "VS Code is not installed."


def open_notepad():

    subprocess.Popen("notepad.exe")

    return "Opening Notepad."


def open_calculator():

    subprocess.Popen("calc.exe")

    return "Opening Calculator."


def open_explorer():

    subprocess.Popen("explorer.exe")

    return "Opening File Explorer."