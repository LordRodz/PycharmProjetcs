def intro():
    # introdução do jogo e breve tutorial
    print('\n' + ('==' * 4) + '\033[1;35mBEM-VINDO: JOGO DA FORCA\033[m' + ('==' * 4))
    print('    \033[4;35monde os espertos não se enforcam\033[m\n')

    while True:
        ver_regras = input('Deseja ver as regras? [Sim] ou [Não] : ').strip().lower()
        if 'sim' in ver_regras:
            print("""Bom, vamos lá.\n
    REGRA número [1] -- O jogador deverá tentar adivinhar a palavra oculta entrando com apenas uma letra por vez.
    REGRA número [2] -- É obrigatório o jogador realizar uma tentativa, caso contrário, isto é, opte por pular a vez, perderá 1 (um) ponto.
    REGRA número [4] -- Tentativas repetidas não contarão como erro.
    REGRA número [5] -- A partida encerrará quando a palavra for totalmente desvendada.""")
            break
        elif 'nao' in ver_regras:
            print('\nOk. Acredito que você seja corajoso ou veterano de meus jogos.')
            break
        elif 'não' in ver_regras:
            print('\nOk. Acredito que você seja corajoso ou veterano de meus jogos.')
        else:
            print('Não compreendi o que quis dizer. Poderia repetir por favor?')
    print('\nDivirta-se e bom jogo.\n')
