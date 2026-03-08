import time

class TableScan:
    def __init__(self, page_manager):
        self.pm = page_manager

    def execute(self, target_word):
        start_time = time.perf_counter()
        current_page = self.pm.first
        pages_scanned = 0

        while current_page is not None:
            pages_scanned += 1
            registers = current_page.get_register()

            for word in registers:
                if word == target_word:
                    end_time = time.perf_counter()
                    return current_page.get_character(), pages_scanned, (end_time - start_time)

            current_page = current_page.next

        end_time = time.perf_counter()
        return None, pages_scanned, (end_time - start_time)