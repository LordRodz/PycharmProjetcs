def ler_arquivo(arquivo):
    """
    lê o arquivo do parâmetro e retorna seu conteúdo em uma variável do tipo lista;
    :param arquivo: arquivo de texto a ser aberto;
    :return: retorna uma lista com os dados presentes
    """
    glossario = list()
    try:
        with open(arquivo, 'rt') as arq:
            for linha in arq:
                glossario.append(linha.replace('\n', ''))
            return glossario
    except FileNotFoundError:
        try:
            criar_arquivo(arquivo)
        except:
            print('Não foi possível criar o arquivo')
    except:
        print('Não foi possível ler ou criar o arquivo')


def criar_arquivo(arquivo):
    """
    checa se existe um arquivo. caso não, cria um para conter as palavras usadas no jogo
    :param arquivo: nome do arquivo para checagem
    :return: retorna o arquivo em modo texto criado
    """
    try:
        with open(arquivo, 'wt+'):
            arquivo.write('')
            return arquivo
    except:
        print('Algo deu errado na criação do arquivo')


def retornar_palavra(arquivo):
    """
    lê o arquivo de palavras e escolhe uma para retorno do jogo da forca
    :param arquivo: nome do arquivo
    :return: uma palavra escolhida aleatóriamente
    """

    from random import choice
    glossario = ler_arquivo(arquivo)
    palavra = choice(glossario)
    return palavra
