from datetime import datetime
import webbrowser
import subprocess



def execute(command):
    command = command.lower()

    # Time
    if "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    # Date
    elif "date" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today is {current_date}"

    # Opens Notepad
    elif "open Notepad" in command:
            subprocess.Popen("notepad.exe")
            return "opening notepad"
    
    # Opens Windows Calculator
    elif "open calculator" in command:
            subprocess.Popen("calc.exe")
            return "opening calculator"

    # Opens Command Prompt
    elif "open cmd" in command:
            subprocess.Popen("cmd.exe")
            return "opening command promt"
    
    # Open Chrome
    elif "open chrome" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Chrome"

    # Open YouTube
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"


    elif "open instagram" in command:
            webbrowser.open("https://www.instagram.com")
            return "Opening instagram"

    # Open ChatGPT
    elif "open chat g p t" in command or "open chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"

    else:
        return None