import requests


def preguntar(prompt):

    payload = {
        "model": "qwen2.5:3b",
        "prompt": f"{SYSTEM_PROMPT}\n\nUsuario: {prompt}",
        "stream": False
    }

    r = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )

    return r.json()["response"]