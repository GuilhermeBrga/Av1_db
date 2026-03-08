from pages.page_manager import page_manager
from reader.read_txt import read_file_txt
from hash.hash_index import HashIndex
from search.table_scan import TableScan
import math


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

        print("\nÍndice Hash Construído!")
        print(f"Taxa de colisão: {hash_index.collision_rate(nr):.2f}%")
        print(f"Taxa de overflow: {hash_index.overflow_rate():.2f}%")

        search_word = input("\nDigite a palavra para busca: ")

        scanner = TableScan(pm)
        result_page = scanner.execute(search_word)

        if result_page is not None:
            print(f"\n[Table Scan] Palavra '{search_word}' encontrada na Página {result_page}.")
        else:
            print(f"\n[Table Scan] Palavra '{search_word}' não encontrada no arquivo.")


        result_hash = hash_index.search(search_word)

        if result_hash is not None:
            print(f"[Hash Index] Palavra '{search_word}' encontrada na Página {result_hash}.")
        else:
            print(f"[Hash Index] Palavra '{search_word}' não encontrada no índice.")

    except ValueError:
                print("Erro: O tamanho da página deve ser um número inteiro válido.")


if __name__ == "__main__":
    main()