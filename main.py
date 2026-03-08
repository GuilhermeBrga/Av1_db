import time
import math
from pages.page_manager import page_manager
from reader.read_txt import read_file_txt
from hash.hash_index import HashIndex
from search.table_scan import TableScan


def main():
    pm = page_manager()
    path = input("Informe o caminho do arquivo de palavras: ")

    try:
        words = read_file_txt(path)
    except IOError:
        print("Erro ao ler o arquivo.")
        return

    print("Total de palavras carregadas:", len(words))
    print("Informe o tamanho da página (registros por página): ", end="")

    try:
        register_per_page = int(input())
        pm.create_page(words, register_per_page)

        pm.show_extreme()

        nr = len(words)
        fr = 4
        nb = math.ceil(nr / fr) + 1
        hash_index = HashIndex(nb, fr)
        hash_index.build_index(pm)

        print(f"\nTaxa de colisão: {hash_index.collision_rate(nr):.2f}%")
        print(f"Taxa de overflow: {hash_index.overflow_rate():.2f}%")

        search_word = input("\nDigite a palavra para busca: ")

        scanner = TableScan(pm)
        res_ts, cost_ts, time_ts = scanner.execute(search_word)

        res_hash, cost_hash, time_hash = hash_index.search(search_word)

        print(f"\nBusca por: {search_word}")
        print(f"Table Scan - Pagina: {res_ts}, Acessos: {cost_ts}, Tempo: {time_ts:.8f}s")
        print(f"Hash Index - Pagina: {res_hash}, Acessos: {cost_hash}, Tempo: {time_hash:.8f}s")

        if time_hash > 0:
            speedup = time_ts / time_hash
            print(f"O Hash Index foi {speedup:.2f} vezes mais rápido.")

    except ValueError:
        print("Erro: O tamanho da página deve ser um número inteiro válido.")


if __name__ == "__main__":
    main()