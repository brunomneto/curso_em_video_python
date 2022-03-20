"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input('\nDigite um número: ')))
    r = str(input('Você deseja acrescentar mais números? [S/N] - ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Opção inválida. Você deseja acrescentar mais números? [S/N] - ')).strip().upper()[0]
    if r == 'N':
        break

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])

print(f'\nA lista completa de números é {lista}')
print(f'Os números pares da lista são: {par}')
print(f'Os números ímpares na lista são: {impar}')
