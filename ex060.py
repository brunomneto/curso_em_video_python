"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""

print('\nCálculo de Fatorial')
n = int(input('Digite um número: '))
f = 1
if n == 0:
    print('0! = 1')
elif n < 0:
    print('Não é possível calcular o fatorial de números negativos.')
else:
    print('{}! = '.format(n), end='')
    while n > 0:
        print('{}'.format(n), end='')
        print(' X ' if n > 1 else ' = ', end='')
        f *= n
        n -= 1
    print('{}'.format(f))
