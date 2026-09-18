import requests
from .prompts import SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"

def consultar_crx(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n\nUsuario: {prompt}",
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json().get("response", "Sin respuesta del motor.")
    except requests.exceptions.RequestException as e:
        return f"[ERROR CRX IA]: No se pudo conectar con el motor local Ollama ({str(e)})"