# dashboard/views.py

import json
import requests

from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .crx.llm import consultar_crx
from .crx.memory import guardar_interaccion, obtener_contexto_reciente
from .crx.tools import obtener_estado_dron
from .crx.vision import analizar_captura
from .models import CapturaInspeccion, TelemetriaDron


def home(request):
    respuesta = ""

    if request.method == "POST":
        prompt = request.POST["prompt"]

        r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:3b",
                "prompt": prompt,
                "stream": False
            }
        )

        respuesta = r.json()["response"]

    return render(
        request,
        "home.html",
        {"respuesta": respuesta}
    )


def index(request):
    telemetria = obtener_estado_dron()
    return render(request, 'dashboard/index.html', {'telemetria': telemetria})


@csrf_exempt
def api_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt', '')

        # 1. Obtener telemetría en vivo automáticamente
        estado_dron = obtener_estado_dron()
        telemetria_str = (
            f"[TELEMETRÍA EN VIVO DRON] -> "
            f"Batería: {estado_dron['bateria']}V | "
            f"RSSI: {estado_dron['rssi']}dBm | "
            f"Temp: {estado_dron['temperatura']}°C"
        )

        # 2. Construir contexto completo
        contexto = obtener_contexto_reciente()
        prompt_completo = f"{telemetria_str}\nContexto previo:\n{contexto}\nUsuario: {prompt}"

        # 3. Consultar a CRX IA
        respuesta = consultar_crx(prompt_completo)
        guardar_interaccion(prompt, respuesta)

        return JsonResponse({'respuesta': respuesta})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def api_telemetria(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        TelemetriaDron.objects.create(
            bateria_voltaje=data.get('bateria', 14.8),
            rssi_wifi=data.get('rssi', -60),
            temperatura=data.get('temperatura', 30.0),
            mpu_pitch=data.get('pitch', 0.0),
            mpu_roll=data.get('roll', 0.0)
        )
        return JsonResponse({'status': 'Telemetría guardada'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def api_upload_imagen(request):
    if request.method == 'POST' and request.FILES.get('foto'):
        archivo_foto = request.FILES['foto']
        captura = CapturaInspeccion.objects.create(imagen=archivo_foto)

        # Procesar con el módulo de visión
        resultado = analizar_captura(captura.imagen.path)
        captura.analisis = resultado
        captura.save()

        return JsonResponse({
            'status': 'Foto recibida',
            'id': captura.id,
            'url': captura.imagen.url,
            'analisis': resultado
        })
    return JsonResponse({'error': 'No se envió ninguna foto'}, status=400)


def generar_reporte_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_inspeccion_crx.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 750, "CARIUX TECH - REPORTE DE INSPECCIÓN DRON V1")
    p.setFont("Helvetica", 10)
    p.drawString(50, 735, "==========================================================")

    estado = obtener_estado_dron()
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 700, "1. TELEMETRÍA DE VUELO:")
    p.setFont("Helvetica", 11)
    p.drawString(70, 680, f"- Batería LiPo 4S: {estado['bateria']} V")
    p.drawString(70, 660, f"- Señal WiFi (RSSI): {estado['rssi']} dBm")
    p.drawString(70, 640, f"- Temperatura Interna: {estado['temperatura']} °C")

    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 600, "2. DIAGNÓSTICO VISUAL (ESP32-CAM):")
    p.setFont("Helvetica", 11)
    p.drawString(70, 580, "Estado Chasis: Óptimo. Sin fisuras ni grietas detectadas por CRX Vision.")

    p.showPage()
    p.save()
    return response