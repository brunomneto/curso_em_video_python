"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep

opcao = ['empate', 'PEDRA', 'PAPEL', 'TESOURA']
print('\033[33m-*-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('JOKENPÔ'))
print('\033[33m-*-\033[m' * 30)
print()
print('\033[37m------------- ESCOLHA SUA JOGADA -------------\033[m')
print('{}'.format('(1) - PEDRA'))
print('{}'.format('(2) - PAPEL'))
print('{}'.format('(3) - TESOURA'))
print('\033[37m----------------------------------------------\033[m')
jogador = int(input('Opção: '))
if jogador < 1 or jogador > 3:
    print('Opção Inválida')
else:
    computador = randint(1, 3)
    print('O computador está pensando', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    print('HORA DE JOGAR!')
    print('\033[37m----------------------------------------------\033[m')
    sleep(1)
    print('JO', end='')
    sleep(1)
    print('KEN', end='')
    sleep(1)
    print('PÔ!')
    if jogador == computador:
        print('O computador escolheu {} e você escolheu {}. \033[33mEMPATE\033[m!'.format(opcao[computador],
                                                                                          opcao[jogador]))
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print('O computador escolheu {} e você escolheu {}. Você \033[32mGANHOU\033[m!'.format(opcao[computador],
                                                                                               opcao[jogador]))
    elif (jogador == 3 and computador == 1) or (jogador == 1 and computador == 2) or (jogador == 2 and computador == 3):
        print('O computador escolheu {} e você escolheu {}. Você \033[31mPERDEU\033[m!'.format(opcao[computador],
                                                                                               opcao[jogador]))
print()
