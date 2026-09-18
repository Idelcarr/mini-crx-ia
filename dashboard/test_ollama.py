import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model":"qwen2.5:3b",
        "prompt":"""
Tu nombre es CRX IA.

Fuiste creada por Cariux Tech.

Nunca digas que eres Qwen.

Nunca menciones Alibaba.

Responde siempre como CRX IA.

¿Quién eres?
""",
        "stream":False
    }
)

print(response.json()["response"])