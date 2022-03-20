"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

print('\033[33m-=-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('QUAL É O MAIOR?'))
print('\033[33m-=-\033[m' * 30)
print()
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print()
if a > b:
    print('O primeiro valor, {}, é maior do que o segundo valor, {}'.format(a, b))
elif a < b:
    print('O segundo valor, {}, é maior do que o primeiro valor, {}.'.format(b, a))
else:
    print('Os dois números, {} e {}, são iguais.'.format(a, b))
