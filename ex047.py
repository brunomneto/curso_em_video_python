"""
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

print('\033[33m-=-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('NÚMEROS PARES - 1 A 50'))
print('\033[33m-=-\033[m' * 30)
print()
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
"""
for c in range(2, 51, 2)
    print (c, end=' ')
"""
print()
print('\033[33m-=-\033[m' * 30)
print('{:^90}'.format('FIM!'))
