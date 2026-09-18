from django.db import models

class MensajeChat(models.Model):
    usuario = models.TextField()
    respuesta_crx = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat {self.fecha.strftime('%Y-%m-%d %H:%M')}"

class TelemetriaDron(models.Model):
    bateria_voltaje = models.FloatField(default=14.8) # Batería LiPo 4S
    rssi_wifi = models.IntegerField(default=-65)
    temperatura = models.FloatField(default=35.0)
    mpu_pitch = models.FloatField(default=0.0)
    mpu_roll = models.FloatField(default=0.0)
    fecha = models.DateTimeField(auto_now_add=True)

class CapturaInspeccion(models.Model):
    imagen = models.ImageField(upload_to='uploads/')
    analisis = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)