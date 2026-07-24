from agents.computer_agent import ComputerAgent
import time

computer = ComputerAgent()

print("Click inside Notepad within 5 seconds...")
time.sleep(5)

computer.write("Hello from Krypton!")
computer.press("enter")
computer.write("Testing keyboard automation.")