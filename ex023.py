""" Exercício Python 23: Faça um programa que leia um número de 0 a 9999
 e mostre na tela cada um dos dígitos separados.

memo = '0000'
print(memo)
num = input('Digite um número de 0 a 9999')
num = ''.join(num.strip().split())
print(num)"""

num = int(input('Digite um número: '))
print('')
print('Analisando o número {}...'.format(num))
print('')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

