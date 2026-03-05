from pages.page_manager import page_manager
from reader.read_txt import read_file_txt
from hash.hash_index import HashIndex
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
        print("Número de Buckets:", nb)
        print("Taxa de colisão:", hash_index.collision_rate(nr), "%")
        print("Taxa de overflow:", hash_index.overflow_rate(), "%")

    except ValueError:
        print("Erro: O tamanho da página deve ser um número inteiro válido.")


if __name__ == "__main__":
    main()