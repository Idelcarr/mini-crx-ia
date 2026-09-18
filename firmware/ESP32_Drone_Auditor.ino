#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "TU_RED_WIFI";
const char* password = "TU_CONTRASEÑA";
const char* serverUrl = "http://192.168.1.XX:8000/api/telemetria/"; // Cambia XX por la IP de tu PC

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Conectado!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    // Simulación de lectura de sensores de voltaje y temperatura
    float bateria = 15.2;
    int rssi = WiFi.RSSI();
    float temp = 32.5;

    String jsonPayload = "{\"bateria\":" + String(bateria) + 
                         ",\"rssi\":" + String(rssi) + 
                         ",\"temperatura\":" + String(temp) + "}";

    int httpCode = http.POST(jsonPayload);
    http.end();
  }
  delay(3000); // Envía telemetría cada 3 segundos
}