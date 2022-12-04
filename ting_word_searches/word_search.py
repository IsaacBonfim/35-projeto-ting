def exists_word(word, instance):
    words_list = list()
    length = len(instance)

    for index in range(length):
        data = instance.search(index)
        lines = data['linhas_do_arquivo']
        found = list()

        for index in range(len(lines)):
            if word.lower() in lines[index].lower():
                found.append(index + 1)

        if len(found):
            words_list.append({
                "palavra": word,
                "arquivo": data['nome_do_arquivo'],
                "ocorrencias": [{"linha": item} for item in found]
            })

    return words_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
