# ========= MAIN - Weather Station =========
# Orquestrador principal do sistema

import time
import ujson

from config import STATION_ID, LOOP_INTERVAL
from network_manager import NetworkManager
from time_manager import TimeManager
from sensors import WeatherSensors
from weather_processing import WeatherProcessor
from storage import StorageManager


def main():

    print("Inicializando sistema...")

    # --- Inicializa módulos ---
    network = NetworkManager()
    clock = TimeManager()
    sensors = WeatherSensors()
    processor = WeatherProcessor()
    storage = StorageManager()

    # --- Conecta WiFi ---
    wifi_connected = network.connect()

    if wifi_connected:
        try:
            clock.sync_ntp()
        except Exception as e:
            print("Falha ao sincronizar NTP:", e)

    print("Sistema iniciado com sucesso.")

    # ========= LOOP PRINCIPAL =========
    while True:
        try:

            # --- Garante conexão ---
            if not network.is_connected():
                network.ensure_connection()

            # --- Coleta dados ---
            raw_data = sensors.read_all()

            # --- Processa dados ---
            processed_data = processor.process(raw_data)

            # --- Timestamp ---
            timestamp = clock.timestamp_iso()

            # --- Monta payload (compatível MicroPython) ---
            payload = {
                "estacao": STATION_ID,
                "timestamp": timestamp
            }

            payload.update(processed_data)

            # --- Armazena localmente ---
            storage.save(payload)

            # --- Debug ---
            print(ujson.dumps(payload))

        except Exception as e:
            print("Erro no loop principal:", e)

        time.sleep(LOOP_INTERVAL)


# ========= ENTRY POINT =========
if __name__ == "__main__":
    main()

