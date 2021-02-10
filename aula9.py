import shutil


def escrever_arquivo(texto):
    diretorio = 'texto.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        # print(lista_notas)
        media = lambda notas: sum([int(nota) for nota in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    diretorio = ''
    shutil.copy(nome_arquivo, diretorio)


def move_arquivo(nome_arquivo):
    diretorio = ''
    shutil.move(nome_arquivo, diretorio)


if __name__ == '__main__':
    move_arquivo('notas.txt')
    copia_arquivo('notas.txt')
    lista_media = media_notas('notas.txt')
    print(lista_media)
    # texto = 'Karla: 9,5,8,9\n'
    # escrever_arquivo(texto)
    # atualizar_arquivo('notas.txt', texto)
    # ler_arquivo('teste.txt')
