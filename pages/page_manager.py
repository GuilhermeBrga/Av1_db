from pages.page import page

def _show_info(page, label):
    if page is None:
        return

    print(f"{label} Página: {page.get_character()}")
    for register in page.get_register()[:5]:
        print(f" - {register}")

class page_manager:
    def __init__(self):
        self.first = None
        self.last = None
        self.total_pages = 0

    def create_page(self, words, register_per_page):
        current = None

        for i in range(len(words)):
            if i % register_per_page == 0:
                num_pag = (i // register_per_page) + 1
                new_page = page(num_pag)

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
        _show_info(self.first, "Primeira")
        _show_info(self.last, "Última")
