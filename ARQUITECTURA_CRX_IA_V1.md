# 🚀 Arquitectura Técnica - CRX IA Mini V1
**Proyecto:** CARIUX DRONE AUDITOR V1  
**Desarrollado por:** Cariux Tech  
**Fase:** Prototipo Académico / Inspección Industrial  

---

## 1. Visión General del Sistema

El sistema **CRX IA Mini** es una plataforma híbrida de inteligencia artificial y telemetría en tiempo real diseñada para misiones de inspección aérea. 

* **Estación Base (Servidor Local):** Backend en Django, base de datos SQLite/PostgreSQL y un motor de LLM local basado en Qwen 2.5 3B servido a través de Ollama.
* **Nodo Aéreo (On-Board):** Módulo ESP32-CAM con sensor OV3660 para transmisión de imágenes y recepción de telemetría (MPU6050, batería 4S, RSSI).

---

## 2. Estructura del Proyecto

```text
Mini CRX IA/
│
├── manage.py
│
├── core/                         # Configuración global del proyecto Django
│   ├── settings.py               # Ajustes principales del sistema
│   ├── urls.py                   # Enrutamiento raíz
│   ├── wsgi.py                   # Despliegue WSGI
│   └── asgi.py                   # Despliegue ASGI (WebSockets / Async)
│
├── dashboard/                    # Aplicación principal
│   ├── migrations/               # Migraciones de base de datos
│   ├── templates/                # Interfaces de usuario (HTML)
│   │   └── dashboard/
│   │       ├── index.html        # Dashboard general de telemetría
│   │       ├── chat.html         # Interfaz de conversación con CRX IA
│   │       └── reports.html      # Visor de reportes de auditoría
│   ├── static/                   # Recursos estáticos (CSS, JS, Imágenes)
│   ├── views.py                  # Vistas y controladores de Django
│   ├── models.py                 # Modelos de BD (Telemetría, Chat, Reportes)
│   ├── urls.py                   # Rutas internas de la app dashboard
│   │
│   └── crx/                      # MÓDULO NÚCLEO - AGENTE CRX IA
│       ├── __init__.py
│       ├── llm.py                # Cliente de comunicación asíncrona con Ollama
│       ├── prompts.py            # Personalidad y System Prompts corporativos
│       ├── memory.py             # Gestión del historial y contexto conversacional
│       ├── vision.py             # Pre-procesamiento de capturas e inspección
│       └── tools.py              # Herramientas de estado del dron y diagnósticos
│
├── uploads/                      # Capturas recibidas desde la ESP32-CAM
├── media/                        # Archivos multimedia del dashboard
├── reports/                      # PDFs de auditoría generados
├── database/                     # Almacenamiento local SQLite
└── ARQUITECTURA_CRX_IA_V1.md     # Documento de arquitectura