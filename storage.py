# ========= STORAGE =========
# Camada de persistência local com rotação

import ujson
import os

from config import BUFFER_FILE, MAX_BUFFER_LINES


class StorageManager:

    def __init__(self):
        self.buffer_file = BUFFER_FILE

    # ==============================
    # Conta linhas do buffer
    # ==============================
    def _count_lines(self):
        try:
            with open(self.buffer_file, "r") as f:
                return sum(1 for _ in f)
        except:
            return 0

    # ==============================
    # Rotação de arquivo
    # ==============================
    def _rotate(self):
        try:
            if "buffer_old.jsonl" in os.listdir():
                os.remove("buffer_old.jsonl")

            os.rename(self.buffer_file, "buffer_old.jsonl")
            print("Buffer rotacionado.")
        except Exception as e:
            print("Erro ao rotacionar:", e)

    # ==============================
    # Salvar payload
    # ==============================
    def save(self, payload):

        try:
            # Verifica rotação
            line_count = self._count_lines()

            if line_count >= MAX_BUFFER_LINES:
                self._rotate()

            # Salva nova linha
            with open(self.buffer_file, "a") as f:
                f.write(ujson.dumps(payload) + "\n")

        except Exception as e:
            print("Erro ao salvar no buffer:", e)

    # ==============================
    # Limpar buffer manualmente
    # ==============================
    def clear(self):
        try:
            os.remove(self.buffer_file)
            print("Buffer limpo.")
        except:
            pass

