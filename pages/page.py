class page:
    def __init__(self, character: int):
        self._character = character
        self._register = []
        self.next = None
        self.previous = None

    def add_register(self, register: str):
        self._register.append(register)

    def get_register(self):
        return self._register

    def get_character(self):
        return self._character


