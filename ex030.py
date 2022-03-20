"""
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
print()
n = int(input('Digite um número: '))
print()
if n % 2 == 0:
    print('O número {} é \033[34mPAR\033[m.'.format(n))
else:
    print('O número {} é \033[31mÍMPAR\033[m.'.format(n))
