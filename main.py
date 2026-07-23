from core.assistant import Assistant
from gui.window import KryptonGUI
import threading

gui = KryptonGUI()

assistant = Assistant(gui)

threading.Thread(
    target=assistant.run,
    daemon=True
).start()

gui.run()