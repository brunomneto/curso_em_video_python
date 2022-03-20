"""
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
"""
print()
print('\033[36m=\033[m'*50)
print('{:^50}'.format('SEQUÊNCIA FIBONACCI'))
print('\033[36m=\033[m'*50)
print()
c = 0
fb1 = 0
fb2 = 1
aux = 0
n = int(input('Informe quantos termos da sequência Fibonacci você quer mostrar: '))
while c < n:
    print('[{}]'.format(fb1))
    aux = fb1 + fb2
    fb1 = fb2
    fb2 = aux
    c += 1
print('FIM!')
