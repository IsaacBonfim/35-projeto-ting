import sys


def txt_importer(path_file):
    try:
        if '.txt' not in path_file:
            return print('Formato inválido', file = sys.stderr)

        with open(path_file) as file:
            info = file.read()
            text = [line for line in info.split('\n')]

            print(text)

            return text

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file = sys.stderr)
