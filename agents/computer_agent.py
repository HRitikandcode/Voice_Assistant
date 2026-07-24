import pyautogui
import pyperclip
import time
import pygetwindow as gw

class ComputerAgent:

    def __init__(self):

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.2

    # ----------------------------------------
    # Mouse
    # ----------------------------------------
    

    def focus_window(self, title):

        windows = gw.getWindowsWithTitle(title)

        if not windows:
            return False

        window = windows[0]

        if window.isMinimized:
            window.restore()

        window.activate()

        time.sleep(0.5)

        return True

    def move(self, x, y):

        pyautogui.moveTo(x, y)

        return "Mouse moved."

    def click(self):

        pyautogui.click()

        return "Clicked."

    def double_click(self):

        pyautogui.doubleClick()

        return "Double clicked."

    def right_click(self):

        pyautogui.rightClick()

        return "Right clicked."

    def drag(self, x, y):

        pyautogui.dragTo(x, y, duration=0.5)

        return "Dragged."

    def scroll(self, amount):

        pyautogui.scroll(amount)

        return "Scrolled."

    # ----------------------------------------
    # Keyboard
    # ----------------------------------------

    def write(self, text):

        pyautogui.write(text, interval=0.03)

        return "Typed."

    def press(self, key):

        pyautogui.press(key)

        return f"Pressed {key}"

    def hotkey(self, *keys):

        pyautogui.hotkey(*keys)

        return f"Pressed {' + '.join(keys)}"

    # ----------------------------------------
    # Clipboard
    # ----------------------------------------

    def copy(self):

        self.hotkey("ctrl", "c")

        return pyperclip.paste()

    def paste(self):

        self.hotkey("ctrl", "v")

        return "Pasted."

    def set_clipboard(self, text):

        pyperclip.copy(text)

        return "Clipboard updated."

    def clipboard(self):

        return pyperclip.paste()

    # ----------------------------------------
    # Screenshot
    # ----------------------------------------

    def screenshot(self, path="screen.png"):

        pyautogui.screenshot(path)

        return path

    # ----------------------------------------
    # Position
    # ----------------------------------------

    def mouse_position(self):

        x, y = pyautogui.position()

        return {
            "x": x,
            "y": y
        }

    def screen_size(self):

        width, height = pyautogui.size()

        return {
            "width": width,
            "height": height
        }

    # ----------------------------------------
    # Wait
    # ----------------------------------------

    def wait(self, seconds):

        time.sleep(seconds)

        return f"Waited {seconds} seconds."