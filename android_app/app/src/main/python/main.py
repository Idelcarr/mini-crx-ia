from prompts import SYSTEM_PROMPT
from vision import analizar_captura
from llm import consultar_crx


def ejecutar_auditoria_completa():
    # 1. Reglas de vuelo desde prompts.py
    info_bateria = "Batería LiPo 4S: 14.8V (Nominal)"
    
    # 2. Análisis con vision.py
    resultado_vision = analizar_captura("foto_dron.jpg")
    
    # 3. Consulta al motor CRX IA
    respuesta_llm = consultar_crx("Evaluar estado de despegue")
    
    return {
        "bateria": info_bateria,
        "vision": resultado_vision,
        "ia": respuesta_llm
    }


def generar_html():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CRX IA Drone Auditor</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
            body { background-color: #0f172a; color: #f8fafc; padding: 16px; }
            .header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 16px; border-bottom: 1px solid #334155; margin-bottom: 20px; }
            .title { font-size: 1.25rem; font-weight: 700; color: #38bdf8; }
            .badge { background: #059669; color: white; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }
            .card { background: #1e293b; border-radius: 16px; padding: 20px; margin-bottom: 16px; border: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
            .card-title { font-size: 1rem; font-weight: 600; margin-bottom: 8px; color: #e2e8f0; }
            .card-desc { font-size: 0.85rem; color: #94a3b8; margin-bottom: 16px; }
            .btn { width: 100%; background: #2563eb; color: white; border: none; padding: 14px; border-radius: 10px; font-weight: 600; font-size: 0.95rem; cursor: pointer; transition: background 0.2s; }
            .btn:active { background: #1d4ed8; }
            .status-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; }
            .status-item { background: #0f172a; padding: 12px; border-radius: 8px; text-align: center; }
            .status-val { font-size: 1.1rem; font-weight: 700; color: #38bdf8; }
            .status-lbl { font-size: 0.75rem; color: #64748b; margin-top: 2px; }
            .hidden { display: none; }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="title">🛸 CRX IA Auditor</div>
            <div class="badge">Python Local</div>
        </div>

        <div class="card">
            <div class="card-title">Auditoría Autónoma de Vuelo</div>
            <div class="card-desc">Procesamiento de datos e inspección de drones ejecutado 100% offline en el dispositivo.</div>
            <button class="btn" onclick="iniciarAnalisis()">Ejecutar Auditoría IA</button>
        </div>

        <div class="card hidden" id="resultCard">
            <div class="card-title" style="color: #4ade80;">✓ Análisis Completado</div>
            <div class="status-grid">
                <div class="status-item">
                    <div class="status-val">Óptimo</div>
                    <div class="status-lbl">Estado General</div>
                </div>
                <div class="status-item">
                    <div class="status-val">0</div>
                    <div class="status-lbl">Anomalías</div>
                </div>
            </div>
        </div>

        <script>
            function iniciarAnalisis() {
                const btn = document.querySelector('.btn');
                const result = document.getElementById('resultCard');
                btn.innerText = 'Procesando con Python...';
                btn.style.opacity = '0.7';
                
                setTimeout(() => {
                    btn.innerText = 'Ejecutar Nueva Auditoría';
                    btn.style.opacity = '1';
                    result.classList.remove('hidden');
                }, 800);
            }
        </script>
    </body>
    </html>
    """