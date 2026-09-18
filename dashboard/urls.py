from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/chat/', views.api_chat, name='api_chat'),
    path('api/telemetria/', views.api_telemetria, name='api_telemetria'),
    path('api/upload/', views.api_upload_imagen, name='api_upload_imagen'),
    path('reporte/pdf/', views.generar_reporte_pdf, name='generar_reporte_pdf'),
]