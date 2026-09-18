package com.cariux.crxia

import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.appcompat.app.AppCompatActivity
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Inicializar Python en Android
        if (!Python.isStarted()) {
            Python.start(AndroidPlatform(this))
        }

        val py = Python.getInstance()
        val mainModule = py.getModule("main") // Carga main.py

        // Invocar la función Python de auditoría
        val resultado = mainModule.callAttr("ejecutar_auditoria_completa").toMap()

        val estadoVision = resultado["vision"].toString()
        val respuestaIA = resultado["ia"].toString()

        // Obtener HTML generado desde Python
        val htmlContent = mainModule.callAttr("generar_html").toString()

        // Configurar y mostrar el contenido en la WebView
        val webView = WebView(this)
        webView.settings.javaScriptEnabled = true
        webView.settings.domStorageEnabled = true
        webView.webViewClient = WebViewClient()

        webView.loadDataWithBaseURL(null, htmlContent, "text/html", "UTF-8", null)
        setContentView(webView)
    }
}