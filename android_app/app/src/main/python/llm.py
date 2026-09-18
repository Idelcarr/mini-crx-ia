import requests
from prompts import SYSTEM_PROMPT

# Reemplaza con la IP de tu PC en la red local (ejemplo) o URL del servidor
OLLAMA_URL = "http://192.168.1.15:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"

def consultar_crx(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n\nUsuario: {prompt}",
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=10)
        return response.json().get("response", "Sin respuesta.")
    except Exception as e:
        return f"[CRX LOCAL]: Modo autónomo activo. (Servidor no alcanzado: {e})"