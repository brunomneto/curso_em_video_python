"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
"""
from time import sleep
from random import randint

computador = randint(0, 10)
contador = 1
print()
print('Eu acabei de pensar em um número, de 0 a 10. Tente adivinhar!')
print()
jogador = int(input('Digite seu palpite: '))
while jogador != computador:
    sleep(0.5)
    contador += 1
    print('Você errou!', end=' ')
    if jogador < 0 or jogador > 10:
        print('Não esqueça, são números de 0 até 10!')
    if jogador > computador:
        jogador = int(input('É menos... tente novamente: '))
    else:
        jogador = int(input('É mais... tente novamente: '))
print('Você acertou! Eu pensei no número {} e você disse {}.'.format(computador, jogador))
print('Você precisou de {} palpite(s) para acertar!'.format(contador))
