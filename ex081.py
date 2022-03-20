"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()
c = 0
while True:
    lista.append(int(input('\nDigite um valor: ')))
    r = str(input('Deseja adicionar mais valores? [S/N] - ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Opção inválida. Deseja adicionar mais valores? [S/N] - ')).strip().upper()[0]
    if r == 'N':
        break

if len(lista) == 1:
    print(f'\nFoi adicionado {len(lista)} valor à lista.')
else:
    print(f'\nForam adicionados {len(lista)} valores à lista.')

lista.sort(reverse=True)
print(f'A lista de números digitada, em ordem decrescente, é: {lista}')

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está presente na lista.')
