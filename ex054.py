"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

print('='*50)
print('{:^50}'.format('GRUPO DA MAIORIDADE'))
print('='*50)
print()

anoatual = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento da pessoa: '))
    if (anoatual - nasc) >= 21:
        maior += 1
    else:
        menor += 1
print()
print('Para este grupo de pessoas, {} atingiram a maioridade e {} não.'.format(maior, menor))
