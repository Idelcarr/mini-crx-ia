import os
from groq import Groq

# Se lee la clave desde las variables de Render, NUNCA expuesta en el código
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def consultar_crx(prompt: str) -> str:
    if not GROQ_API_KEY:
        return "[ERROR CRX IA]: La API Key de Groq no está configurada en las variables de Render."

    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            model="qwen3.8-7b",
            messages=[
                {"role": "system", "content": "Eres CRX IA, un asistente experto para auditoría y control de drones."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"[ERROR CRX IA]: {str(e)}"