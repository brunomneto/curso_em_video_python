"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
from time import sleep
print()
print('=' * 60)
print('{:^60}'.format('BANCO 24 HORAS'))
print('=' * 60)
print()
n = int(input('Digite o valor a ser sacado: R$ '))
cinq = n // 50
vinte = (n % 50) // 20
dez = ((n % 50) % 20) // 10
um = (((n % 50) % 20) % 10) // 1
print()
print('=' * 60)
print(f'O valor de R$ {n} será sacado em notas de: ')
sleep(1)
print(f'\n{cinq:^5} cédulas de R$ 50')
print(f'{vinte:^5} cédulas de R$ 20')
print(f'{dez:^5} cédulas de R$ 10')
print(f'{um:^5} cédulas de R$  1')
print()
print('=' * 60)
sleep(1)
print('ATÉ LOGO. O BANCO 24 HORAS TE ESPERA!')
print('=' * 60)
