"""
Exercício Python 28: Escreva um programa que faça o computador “pensar”
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep
computador = randint(0, 5)
print()
jogador = int(input('Qual é o número de 0 a 5 que o computador acabou de pensar? '))
print()
print('PROCESSANDO...')
print()
sleep(3)
if jogador == computador:
    print('\033[32mParabéns, você acertou!\033[m')
else:
    print('\033[31mErrou! Você disse {}, mas a resposta correta era {}.\033[m'.format(jogador, computador))
