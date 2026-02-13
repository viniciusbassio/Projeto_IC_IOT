# ========= NETWORK MANAGER =========
# Gerenciamento robusto de WiFi

import network
import time

from config import WIFI_SSID, WIFI_PASSWORD


class NetworkManager:

    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    # ==============================
    # Conectar WiFi
    # ==============================
    def connect(self, timeout=15):
        if self.wlan.isconnected():
            print("WiFi já conectado:", self.wlan.ifconfig())
            return True

        print("Conectando ao WiFi...")
        self.wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        start_time = time.time()

        while not self.wlan.isconnected():
            if time.time() - start_time > timeout:
                print("Timeout ao conectar WiFi.")
                return False
            time.sleep(1)

        print("WiFi conectado:", self.wlan.ifconfig())
        return True

    # ==============================
    # Verificar conexão
    # ==============================
    def is_connected(self):
        return self.wlan.isconnected()

    # ==============================
    # Garantir conexão (reconectar se cair)
    # ==============================
    def ensure_connection(self):
        if not self.wlan.isconnected():
            print("WiFi desconectado. Tentando reconectar...")
            return self.connect()
        return True

    # ==============================
    # Desconectar manualmente
    # ==============================
    def disconnect(self):
        if self.wlan.isconnected():
            self.wlan.disconnect()
            print("WiFi desconectado.")

