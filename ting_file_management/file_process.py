from .file_management import txt_importer
import sys


def process(path_file, instance):
    path = None

    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            path = instance.search(index)

    if path is None:
        data = txt_importer(path_file)
        lines = len(data)
        item = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': lines,
            'linhas_do_arquivo': data
        }
        instance.enqueue(item)
        sys.stdout.write(f"{item}")


def remove(instance):
    if not len(instance):
        sys.stdout.write('Não há elementos\n')
        return

    item = instance.dequeue()
    print(item)

    path = item['nome_do_arquivo']

    sys.stdout.write(f"Arquivo {path} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(f"{instance.search(position)}")
    except IndexError:
        sys.stderr.write('Posição inválida\n')
