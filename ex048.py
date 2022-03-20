"""
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
"""
print('\033[33m-=-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('CALCULADORA ESPECIAL - SOMA DOS ÍMPARES, MÚLTIPLOS DE 3 - 1 A 500'))
print('\033[33m-=-\033[m' * 30)
soma = 0
for c in range(1, 501):  # posso usar for c in range(1, 501, 2) para pular o primeiro if.
    if c % 2 == 1:
        if c % 3 == 0:
            print(c, end=' ')
            soma += c
print()
print('A soma dos números ímpares, múltiplos de 3 entre 1 e 500 é igual a {}!'.format(soma))
