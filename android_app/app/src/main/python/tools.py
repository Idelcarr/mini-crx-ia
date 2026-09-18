from dashboard.models import TelemetriaDron

def obtener_estado_dron() -> dict:
    ultima_telemetria = TelemetriaDron.objects.last()
    if not ultima_telemetria:
        return {
            "bateria": 14.8,
            "rssi": -60,
            "estado": "Sin datos de telemetría registrados"
        }
    return {
        "bateria": ultima_telemetria.bateria_voltaje,
        "rssi": ultima_telemetria.rssi_wifi,
        "temperatura": ultima_telemetria.temperatura,
        "pitch": ultima_telemetria.mpu_pitch,
        "roll": ultima_telemetria.mpu_roll
    }