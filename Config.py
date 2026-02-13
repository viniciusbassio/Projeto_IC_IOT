# ========= CONFIG - Weather Station =========
# Arquivo central de configuração do sistema


# ==============================
# IDENTIFICAÇÃO DA ESTAÇÃO
# ==============================
STATION_ID = "adamantina_01"


# ==============================
# REDE
# ==============================
WIFI_SSID = "SUA REDE WIFI"
WIFI_PASSWORD = "SUA SENHA"

NTP_UTC_OFFSET = -3  # Brasil UTC-3


# ==============================
# LOOP PRINCIPAL
# ==============================
LOOP_INTERVAL = 60  # segundos entre leituras


# ==============================
# I2C - BMP280
# ==============================
I2C_SCL_PIN = 22
I2C_SDA_PIN = 21
BMP280_ADDRESS = 0x76


# ==============================
# ADC - GUVA-S12SD
# ==============================
UV_ADC_PIN = 34
UV_ADC_ATTENUATION = 11  # 11dB (0-3.3V)
UV_ADC_WIDTH = 12  # 12 bits (0-4095)

UV_SAMPLE_COUNT = 20  # amostras para filtro


# ==============================
# METEOROLOGIA
# ==============================
SEA_LEVEL_PRESSURE = 1013.25  # hPa (média padrão)
STATION_ALTITUDE = 400  # metros (Adamantina aprox)


# ==============================
# STORAGE
# ==============================
BUFFER_FILE = "buffer.json"
MAX_BUFFER_LINES = 500  # rotação futura


# ==============================
# MQTT (FUTURO)
# ==============================
MQTT_ENABLED = False
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "weather/adamantina"

