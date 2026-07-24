import time

from ai import ask

from agents.browser_agent import BrowserAgent
from agents.computer_agent import ComputerAgent

from tools.app_tools import (
    open_chrome,
    open_vscode,
    open_notepad,
    open_calculator,
    open_explorer,
)


class Brain:

    def __init__(self):

        self.browser = BrowserAgent()
        self.computer = ComputerAgent()

    def process(self, command):

        command = command.strip()

        lower = command.lower()

        # ----------------------------------
        # Applications
        # ----------------------------------

        if "open chrome" in lower:
            return open_chrome()

        if "open vscode" in lower or "open vs code" in lower:
            return open_vscode()

        if "open calculator" in lower:
            return open_calculator()

        if "open explorer" in lower or "open file explorer" in lower:
            return open_explorer()

        # ----------------------------------
        # Notepad
        # ----------------------------------

        if lower == "open notepad":
            return open_notepad()

        if lower.startswith("open notepad and type"):

            text = command[len("open notepad and type"):].strip()

            open_notepad()

            time.sleep(1.5)

            self.computer.write(text)

            return "Done Boss."

        # ----------------------------------
        # Type Anywhere
        # ----------------------------------

        if lower.startswith("type "):

            text = command[5:]      # keeps original capitalization

            self.computer.write(text)

            return "Typed."

        if lower == "press enter":

            self.computer.press("enter")

            return "Pressed Enter."

        if lower == "copy":

            self.computer.hotkey("ctrl", "c")

            return "Copied."

        if lower == "paste":

            self.computer.hotkey("ctrl", "v")

            return "Pasted."

        if lower == "select all":

            self.computer.hotkey("ctrl", "a")

            return "Selected everything."

        # ----------------------------------
        # Browser
        # ----------------------------------

        if lower.startswith("open website"):

            url = command[len("open website"):].strip()

            return self.browser.open(url)

        
        if lower.startswith("open notepad and type"):

            text = command[len("open notepad and type"):].strip()

            open_notepad()

            time.sleep(1)

            self.computer.focus_window("Notepad")

            self.computer.write(text)

            return "Done Boss."

        if lower == "browser back":
            return self.browser.back()

        if lower == "browser forward":
            return self.browser.forward()

        if lower == "browser refresh":
            return self.browser.refresh()

        # ----------------------------------
        # Screenshot
        # ----------------------------------

        if lower == "take screenshot":

            path = self.computer.screenshot()

            return f"Screenshot saved to {path}"

        # ----------------------------------

        return ask(command)