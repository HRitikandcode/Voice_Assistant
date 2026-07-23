from ollama import chat
from config import MODEL_NAME
from core.memory import Memory

memory = Memory()


def ask(prompt):

    memory.add_user(prompt)

    response = chat(
        model=MODEL_NAME,
        messages=memory.get_messages()
    )

    reply = response["message"]["content"]

    memory.add_assistant(reply)

    memory.trim()

    return reply