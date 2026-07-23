from commands import execute
from ai import ask


class Brain:

    def process(self, command):

        command = command.lower().strip()

        # First try local tools
        response = execute(command)

        if response is not None:
            return response

        # Otherwise ask the AI
        return ask(command)