class TableScan:
    def __init__(self, page_manager):
        self.pm = page_manager

    def execute(self, target_word):
        current_page = self.pm.first

        while current_page is not None:
            registers = current_page.get_register()

            for word in registers:
                if word == target_word:
                    return current_page.get_character()

            current_page = current_page.next

        return None