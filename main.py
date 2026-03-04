from pages.page_manager import page_manager
from reader.read_txt import read_file_txt

def main():
    pm = page_manager()

    path = input("Informe o caminho do arquivo de palavras: ")

    try:
        words = read_file_txt(path)
    except IOError:
        print("Erro ao ler o arquivo.")
        return



    for word in words:
        print(word)

    print("Informe o tamanho da página (registros por página): ", end="")

    try:
        register_per_page = int(input())
        pm.create_page(words, register_per_page)
        pm.show_extreme()

    except ValueError:
        print("Erro: O tamanho da página deve ser um número inteiro válido.")

if __name__ == "__main__":
    main()
