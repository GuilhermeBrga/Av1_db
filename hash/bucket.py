class Bucket:
    def __init__(self, fr):
        self.fr = fr  # capacidade do bucket
        self.entries = []  # lista de (chave, numero_pagina)
        self.overflow = None  # bucket de overflow

    def is_full(self):
        return len(self.entries) >= self.fr