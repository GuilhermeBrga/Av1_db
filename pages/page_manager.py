from pages.page import page
import math

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
        self.total_pages = math.ceil(len(words) / register_per_page)

        current_node = None

        for i in range(0, len(words), register_per_page):
            page_num = (i // register_per_page) + 1
            new_page = page(page_num)

            page_content = words[i: i + register_per_page]
            for word in page_content:
                new_page.add_register(word)

            if self.first is None:
                self.first = new_page
            else:
                current_node.next = new_page
                new_page.previous = current_node

            current_node = new_page
            self.last = new_page

    def show_extreme(self):
        _show_info(self.first, "Primeira")
        _show_info(self.last, "Última")
