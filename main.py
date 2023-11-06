from jogo_da_forca.visual import *
from jogo_da_forca.arquivos import *

jogo = True
resposta = retornar_palavra('arquivo.txt').strip().upper()
palavra_escondida = list()
erros = 10

for r in resposta:
    palavra_escondida.append('[*]')

intro()
print(palavra_escondida, '\n')

while jogo:
    # corpo do jogo
    tentativa = str(input('Letra: ')).upper().strip()
    v = True
    for i, l in enumerate(resposta):  # indice, letra
        if l == tentativa:
            palavra_escondida[i] = l
            v = False
    else:
        if v:
            erros -= 1
            print(f'Quantidade de erros: {erros}')
            v = False
    print(palavra_escondida)
    fim = palavra_escondida.count('[*]')
    if erros == 0:
        print('Fim de jogo. Você foi enforcado!')
        print(f'A palavra escondida era: {resposta}. Mais sorte na próxima vez')
        jogo = False
    elif fim == 0:
        print('Fim de jogo. Você se salvou da forca')
        jogo = False
