"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
print('='*50)
print('{:^50}'.format('TABELA DE PESOS'))
print('='*50)
print()

for c in range(0, 5):
    peso = float(input('Digite o peso da pessoa, em kg: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print()
print('Dentre os pesos digitados, o maior peso é {:.1f}kg e o menor peso é {:.1f}kg'.format(maior, menor))
