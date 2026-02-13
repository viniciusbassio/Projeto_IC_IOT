# ========= TIME MANAGER =========
# Gerenciamento de horário e NTP

import time
import ntptime

from config import NTP_UTC_OFFSET


class TimeManager:

    def __init__(self):
        self.utc_offset_seconds = NTP_UTC_OFFSET * 3600

    # ==============================
    # Sincroniza NTP
    # ==============================
    def sync_ntp(self):
        try:
            ntptime.settime()
            print("Horário sincronizado via NTP")
        except Exception as e:
            print("Erro ao sincronizar NTP:", e)

    # ==============================
    # Timestamp ISO Brasil
    # ==============================
    def timestamp_iso(self):
        try:
            current_time = time.time() + self.utc_offset_seconds
            t = time.localtime(current_time)

            return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(
                t[0], t[1], t[2],
                t[3], t[4], t[5]
            )

        except:
            # fallback se NTP ainda não sincronizou
            return "1970-01-01T00:00:00"

