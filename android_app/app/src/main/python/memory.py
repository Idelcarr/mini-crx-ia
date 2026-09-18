from dashboard.models import MensajeChat

def guardar_interaccion(prompt_usuario: str, respuesta_crx: str):
    MensajeChat.objects.create(
        usuario=prompt_usuario,
        respuesta_crx=respuesta_crx
    )

def obtener_contexto_reciente(limite: int = 3) -> str:
    mensajes = MensajeChat.objects.order_by('-fecha')[:limite]
    contexto = ""
    for msg in reversed(mensajes):
        contexto += f"Usuario: {msg.usuario}\nCRX IA: {msg.respuesta_crx}\n"
    return contexto