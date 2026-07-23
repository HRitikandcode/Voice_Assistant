from personality import SYSTEM_PROMPT

class Memory:

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        
    def add_user(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

    def add_assistant(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })

    def get_messages(self):
        return self.messages

    def trim(self, max_messages=20):
        if len(self.messages) > max_messages:
            self.messages = [
                self.messages[0],          # Keep system prompt
                *self.messages[-(max_messages - 1):]
            ]