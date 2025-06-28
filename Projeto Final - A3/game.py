import os, random, time

# limpa a tela do console
def limparTela():
    os.system('cls') # isso é específico para windows

# solicita o nome do jogador
def pegarNomeJogador(nJogador):
    while (True):
        nome = input(f'DIGITE O NOME DO {nJogador}º JOGADOR: ').strip()
        if (len(nome) != 0):
            return nome
        else:
            print('INFORME UM NOME VÁLIDO, POR FAVOR!')

# cria e exibe o tabuleiro com a posição dos jogadores
def criarTabuleiro(tamanho, posicaoP1, posicaoP2, cpuGamer = False):
    tabuleiro = ['_'] * tamanho # tabuleiro vazio

    # preenche a posição do 1º jogador
    if (posicaoP1 < tamanho):
        tabuleiro[posicaoP1] = 'P1'
    
    # preenche a posição do 2º jogador ou CPU, evitando sobreescrever se estiverem na mesma casa
    # e garantindo que o indicador seja 'CPU' se for um jogo de P1 vs CPU
    if (posicaoP2 < tamanho):
        if (posicaoP1 == posicaoP2):
            tabuleiro[posicaoP1] = 'X' # 'X' indica que ambos estão na mesma casa
        else:
            tabuleiro[posicaoP2] = 'P2' if not cpuGamer else 'CPU'

    # formatação visual
    print('\n' + ' '.join(tabuleiro))
    # garante que o número de espaços não seja negativo
    espacos = max(0, tamanho * 2 - 10) 
    print(f'INICÍO {' ' * espacos} FIM')
    print('-' * (tamanho * 2 + 5))

def girarDado():
    return random.randint(1, 3)

# retorna uma pergunta e sua resposta correta
def pegarPergunta():
    perguntas = [
        {'pergunta': 'QUAL A CAPITAL DA FRANÇA?', 'resposta': 'PARIS'},
        {'pergunta': 'QUEM O PRIMEIRO NOME DE QUEM DESCOBRIU O BRASIL?', 'resposta': 'PEDRO'},
        {'pergunta': 'QUANTOS CONTINENTES EXISTEM NO MUNDO?', 'resposta': '7'},
        {'pergunta': 'QUAL O MAIOR OCEANO DA TERRA?', 'resposta': 'PACÍFICO'},
        {'pergunta': 'QUAL O SÍMBOLO QUÍMICO DA ÁGUA?', 'resposta': 'H2O'},
        {'pergunta': 'QUAL A COR DO CAVALO BRANCO DE NAPOLEÃO?', 'resposta': 'BRANCO'},
        {'pergunta': 'QUANTO É 7X8?', 'resposta': '56'},
        {'pergunta': 'QUANTO É 1+1', 'resposta': '2'},
        {'pergunta': 'O QUE A VACA BEBE?', 'resposta': 'ÁGUA'},
        {'pergunta': 'QUAL A MONTANHA MAIS ALTA DO MUNDO?', 'resposta': 'EVEREST'}
    ]
    return random.choice(perguntas)

# simula a resposta da CPU
# a CPU tem 70% de chance de acertar e 30% de errar
def cpuRespostaCorreta():
    if (random.random() < 0.7): # 70%
        print('A CPU PENSOU E RESPONDEU: *RESPOSTA CORRETA!*')
        return True
    else: # 30%
        print('A CPU PENSOU E RESPONDEU: *RESPOSTA INCORRETA!* ')
        return False

# função principal do jogo
def main():
    limparTela()
    print('BEM-VINDO AO JOGO')
    print('O PRIMEIRO A CHEGAR AO FINAL... VENCE!\n')

    nomeP1 = pegarNomeJogador(1)
    nomeP2 = 'CPU' # valor padrão, será alterado se 1x1
    cpuGamer = False # valor padrão, será True se 1 x CPU

    # escolha o modelo de jogo
    while (True):
        try:
            modelo = int(input('DIGITE 1 PARA JOGAR 1X1 OU 2 PARA JOGAR CONTRA A CPU: '))
            if (modelo == 1):
                nomeP2 = pegarNomeJogador(2) # pede o nome do P2, se não for CPU
                cpuGamer = False # garante que cpuGamer é False para 1x1
                break # sai do loop de escolha de modelo de jogo
            elif (modelo == 2):
                cpuGamer = True # define cpuGamer como True para 1xCPU
                break # sai do loop de escolha de modo
            else:
                print('OPÇÃO INVÁLIDA! DIGITE 1 OU 2')
                time.sleep(3)
                limparTela()
        except ValueError:
            print('ENTRADA INVÁLIDA! POR FAVOR, DIGITE UM NÚMERO (1 OU 2).')
            time.sleep(3)
            limparTela()

    tamanhoTabuleiro = 10 
    posicaoP1 = 0 
    posicaoP2 = 0 

    jogadorAtual = 1 # 1 para P1 ou 2 para P2/CPU

    # laço principal do jogo
    while (posicaoP1 < tamanhoTabuleiro - 1 and posicaoP2 < tamanhoTabuleiro - 1):
        limparTela()
        criarTabuleiro(tamanhoTabuleiro, posicaoP1, posicaoP2, cpuGamer)

        nomeJogadorAtivo = nomeP1 if jogadorAtual == 1 else nomeP2
        posicaoJogadorAtivo = posicaoP1 if jogadorAtual == 1 else posicaoP2

        print(f'É A VEZ DE {nomeJogadorAtivo} (POSIÇÃO ATUAL: {posicaoJogadorAtivo + 1} / {tamanhoTabuleiro})') 
        
        input('PRESSIONE ENTER PARA LANÇAR O DADO E PEGAR SUA PERGUNTA... ') 

        giroDado = girarDado()
        print(f'VOCÊ TIROU: {giroDado} NO DADO!') 
        time.sleep(1.5) 

        valorPergunta = pegarPergunta()
        pergunta = valorPergunta['pergunta']
        respostaCorreta = valorPergunta['resposta'].upper() 

        acertouResposta = False

        # lógica de pergunta e resposta para o JOGADOR ou CPU
        if (jogadorAtual == 1): # vez do P1
            print(f'\nPERGUNTA PARA O {nomeJogadorAtivo}:')
            print(pergunta)
            respostaJogador = input('SUA RESPOSTA: ').strip().upper() 
            acertouResposta = (respostaJogador == respostaCorreta)
            if not (acertouResposta):
                print(f'A RESPOSTA CORRETA ERA: {valorPergunta["resposta"]}.') 
        else: # vez do P2
            if cpuGamer: # Se o modo de jogo for 1 x CPU e for a vez do P2
                print(f'\nPERGUNTA PARA O {nomeJogadorAtivo}: {pergunta}')
                time.sleep(2) # para simular o tempo de pensamento da CPU
                acertouResposta = cpuRespostaCorreta() # CPU responde
                if not (acertouResposta):
                    print(f'A RESPOSTA CORRETA ERA: {valorPergunta["resposta"]}.')
            else: # se o modo de jogo for 1x1 e for a vez do P2
                print(f'\nPERGUNTA PARA O {nomeJogadorAtivo}:')
                print(pergunta)
                respostaJogador = input('SUA RESPOSTA: ').strip().upper() 
                acertouResposta = (respostaJogador == respostaCorreta)
                if not (acertouResposta):
                    print(f'A RESPOSTA CORRETA ERA: {valorPergunta["resposta"]}.')

        # estrutura de decisão para atualizar a posição
        if (acertouResposta): 
            print('\nPARABÉNS! RESPOSTA CORRETA!' if jogadorAtual == 1 else '\nCPU ACERTOU!' if cpuGamer else '\nPARABÉNS! RESPOSTA CORRETA!')
            print(f'AVANÇA {giroDado} CASAS!')
            if (jogadorAtual == 1):
                posicaoP1 = min(tamanhoTabuleiro - 1, posicaoP1 + giroDado)
            else:
                posicaoP2 = min(tamanhoTabuleiro - 1, posicaoP2 + giroDado)
        else:
            print('\nRESPOSTA INCORRETA!' if jogadorAtual == 1 else '\nCPU ERROU!' if cpuGamer else '\nRESPOSTA INCORRETA!')
            print(f'RECUA {giroDado} CASAS!')
            if (jogadorAtual == 1):
                posicaoP1 = max(0, posicaoP1 - giroDado)
            else:
                posicaoP2 = max(0, posicaoP2 - giroDado)
            
        time.sleep(2.5) 

        # alterna o jogador
        jogadorAtual = 3 - jogadorAtual

    # fim do jogo
    limparTela()
    criarTabuleiro(tamanhoTabuleiro, posicaoP1, posicaoP2, cpuGamer)
    print('\n----- FIM DE JOGO! -----')

    if (posicaoP1 >= tamanhoTabuleiro - 1):
        print(f'PARABÉNS, {nomeP1}! VOCÊ VENCEU O JOGO!')
    else:
        print(f'PARABÉNS, {nomeP2}! VOCÊ VENCEU O JOGO!')
    
    print('\nOBRIGADO POR JOGAR!')

# chamada principal do jogo
main()