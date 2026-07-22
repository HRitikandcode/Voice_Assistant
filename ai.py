from ollama import chat
from config import MODEL_NAME

def ask(prompt):

    response = chat(
        model=MODEL_NAME,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]