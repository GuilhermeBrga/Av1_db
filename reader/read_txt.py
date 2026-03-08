def read_file_txt(path: str) -> list:
    with open(path, 'r') as archive:
        return archive.read().splitlines()
