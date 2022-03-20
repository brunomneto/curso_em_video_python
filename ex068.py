"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
"""
from random import randint
from time import sleep
print()
print('=-' * 40)
print('{:^80}'.format('JOGO DO PAR OU ÍMPAR'))
print('=-' * 40)
pcpi = ' '
soma = vitoria = 0
while True:
    jg = int(input('\nDigite um valor: '))
    pc = randint(0, 99)
    jgpi = str(input('Você quer par ou ímpar? [P/I] - ')).strip().upper()[0]
    while jgpi not in 'PI':
        jgpi = str(input('Opção Inválida, escolha par ou ímpar: [P/I] - ')).strip().upper()[0]
    soma = jg + pc
    print(f'Você escolheu {jg} e eu escolhi {pc}. A soma deu {soma}: ', end='')
    print('PAR!' if soma % 2 == 0 else 'ÍMPAR!')
    sleep(1)
    if jgpi == 'P':
        if soma % 2 == 0:
            print('Você GANHOU! Vamos jogar novamente! :D')
            vitoria += 1
            sleep(1)
        else:
            print('GAME OVER pra você!')
            sleep(1)
            break
    elif jgpi == 'I':
        if soma % 2 == 1:
            print('Você GANHOU! Vamos jogar novamente! :D')
            vitoria += 1
            sleep(1)
        else:
            print('GAME OVER pra você!')
            sleep(1)
            break
print(f'\nVocê ganhou {vitoria} partida(s).')
