lista = list()
dados = list()
tot = maior = menor = 0
print('-=' * 30)
print('{:^60}'.format('Lista de Pessoas'))
print('-=' * 30)

while True:
    print()
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso em kg: ')))
    lista.append(dados[:])
    tot += 1
    dados.clear()
    r = str(input('Você quer cadastrar mais nomes? [S/N] - ')).strip().upper()
    while r not in 'SN':
        r = str(input('Opção inválida. Você quer cadastrar mais nomes? [S/N] - ')).strip().upper()
    if r == 'N':
        break

for p in range(0, len(lista)):
    if p == 0:
        menor = maior = lista[p][1]
    else:
        if lista[p][1] < menor:
            menor = lista[p][1]
        elif lista[p][1] > maior:
            maior = lista[p][1]

print('-=' * 30)
print(f'\nForam cadastradas {tot} pessoas.')
print('O maior peso é de {:.1f}kg. '.format(maior), end='')
print('Este é o peso de: ', end='')
for p in lista:
    if p[1] == maior:
        print(p[0], end=' ')
print('\nO menor peso é de {:.1f}kg. '.format(menor), end='')
print('Este é o peso de: ', end='')
for p in lista:
    if p[1] == menor:
        print(p[0], end=' ')
