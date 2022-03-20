"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""

valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('O número já existe na lista.')
    else:
        valores.append(n)
    r = str(input('\nQuer adicionar mais números? [S/N] - ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Resposta inválida. Quer adicionar mais números? [S/N] - ')).strip().upper()[0]
    if r == 'N':
        break
valores.sort()
print(f'\nOs números digitados são os seguintes: {valores}')
