class Page:
    def __init__(self, register: int):
        self._register = register
        self._registers = []
        self.next = None
        self.previous = None

    def add_register(self, register: str):
        self._registers.append(register)

    def get_register(self):
        return self._registers

    def get_character(self):
        return self._register
