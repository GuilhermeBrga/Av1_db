from reader import read_txt

archive_path = input("Informe o caminho do arquivo txt: ")

db_list = read_txt.read_file_txt(archive_path)

print(db_list)