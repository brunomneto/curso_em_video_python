"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
from time import sleep
print()
print('=-' * 40)
print('{:^80}'.format('MERCADÃO DA PROMOÇÃO'))
print('=-' * 40)
nome = continuar = nomebarato = ''
preco = total = precobarato = maisdemil = qtd = 0

while True:
    nome = str(input('\nNome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    qtd += 1
    total += preco
    if preco > 1000:
        maisdemil += 1
    if qtd == 1 or preco < precobarato:
        precobarato = preco
        nomebarato = nome
    continuar = str(input('Incluir mais produtos na lista? [S/N] - ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção Inválida. Incluir mais produtos? [S/N] - ')).strip().upper()[0]
    if continuar == 'N':
        print('\nFINALIZANDO...')
        sleep(2)
        break
print(f'\nTotal de compras - R$ {total:.2f}')
print(f'{maisdemil} produto(s) com preço acima de R$ 1000.00')
print(f'O produto mais barato da lista é {nomebarato} e custou R$ {precobarato:.2f}.')
