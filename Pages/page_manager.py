class Page:
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



class PageManager:
    def __init__(self):
        self.first = None
        self.last = None
        self.total_pages = 0

    def create_page(self, words, register_per_page):
        if register_per_page <= 0:
            return

        current = None

        for i in range(len(words)):
            if i % register_per_page == 0:
                num_pag = (i // register_per_page) + 1
                new_page = Page(num_pag)

                if self.first is None:
                    self.first = new_page
                else:
                    current.next = new_page
                    new_page.previous = current

                current = new_page
                self.last = new_page
                self.total_pages += 1

            current.add_register(words[i])

    def show_extreme(self):
        self._show_info(self.first, "Primeira")
        self._show_info(self.last, "Última")


    def _show_info(self, page, label):
        if page is None:
            return

        print(f"{label} Página: {page.get_character()}")
        for register in page.get_register()[:5]:
            print(f" - {register}")




