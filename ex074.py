"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# menor = 0
# maior = 0

print('\nOs números sorteados são: ', end='')
for c in range(0, len(tupla)):
    print(tupla[c], end='  ')
    """if c == 0:
        menor = tupla[c]
        maior = tupla[c]
    else:
        if tupla[c] < menor:
            menor = tupla[c]
        if tupla[c] > maior:
            maior = tupla[c]"""

print(f'\n\nO maior número é {max(tupla)} e o menor é {min(tupla)}.')
