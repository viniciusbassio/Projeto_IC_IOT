from machine import Pin
import dht
import time
import ujson
import network
import ntptime
import os

# ========= WIFI =========
SSID = "NOME DA SUA REDE"
PASSWORD = "SENHA DA SUA REDE"

wlan = network.WLAN(network.STA_IF)

def conecta_wifi():
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando ao WiFi...")
        wlan.connect(SSID, PASSWORD)

        timeout = 10
        start = time.time()
        while not wlan.isconnected():
            if time.time() - start > timeout:
                print("Falha ao conectar no WiFi")
                return False
            time.sleep(1)

    print("WiFi conectado:", wlan.ifconfig())
    return True


def wifi_ok():
    return wlan.isconnected()


# ========= SINCRONIZA NTP =========
def sincroniza_hora():
    try:
        ntptime.settime()
        print("Horário sincronizado via NTP")
    except:
        print("Falha ao sincronizar NTP")


# ========= CONVERTE PARA ISO =========
def timestamp_iso():
    utc_offset = -3 * 3600  # UTC-3 Brasil
    t = time.localtime(time.time() + utc_offset)

    return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(
        t[0], t[1], t[2], t[3], t[4], t[5]
    )


# ========= BUFFER LOCAL =========
BUFFER_FILE = "buffer.jsonl"

def salvar_buffer(dados):
    try:
        with open(BUFFER_FILE, "a") as f:
            f.write(ujson.dumps(dados) + "\n")
        print("Salvo no buffer")
    except Exception as e:
        print("Erro ao salvar buffer:", e)


def enviar_dado(dado):
    """
    Aqui futuramente você coloca:
    - HTTP POST
    - MQTT publish
    - Envio para API
    """
    print("Enviando:", ujson.dumps(dado))
    return True  # Simulando sucesso


def reenviar_buffer():
    if not wifi_ok():
        return

    if BUFFER_FILE not in os.listdir():
        return

    try:
        with open(BUFFER_FILE, "r") as f:
            linhas = f.readlines()
    except:
        return

    if not linhas:
        return

    print("Reenviando dados do buffer...")

    enviados = []

    for linha in linhas:
        try:
            dado = ujson.loads(linha.strip())
            if enviar_dado(dado):
                enviados.append(linha)
            else:
                break
        except:
            break

    # Se enviou tudo, limpa buffer
    if len(enviados) == len(linhas):
        open(BUFFER_FILE, "w").close()
        print("Buffer limpo")


# ========= SENSORES =========
sensor = dht.DHT11(Pin(4))
ldr = Pin(23, Pin.IN)

# ========= INICIALIZA =========
conecta_wifi()
sincroniza_hora()

while True:
    try:

        # Se WiFi caiu, tenta reconectar
        if not wifi_ok():
            conecta_wifi()

        sensor.measure()

        temperatura = sensor.temperature()
        umidade = sensor.humidity()
        luz = ldr.value()

        estado_luz = "CLARO" if luz == 0 else "ESCURO"

        dados = {
            "estacao": "adamantina_01",
            "timestamp": timestamp_iso(),
            "temperatura": temperatura,
            "umidade": umidade,
            "luminosidade": estado_luz
        }

        # Se tiver internet, envia
        if wifi_ok():
            if enviar_dado(dados):
                reenviar_buffer()
            else:
                salvar_buffer(dados)
        else:
            salvar_buffer(dados)

    except Exception as e:
        print("Erro:", e)

    time.sleep(60)

