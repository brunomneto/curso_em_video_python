"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
print()
print('\033[36m=\033[m'*100)
print('{:^100}'.format('MÉDIA, MAIOR E MENOR'))
print('\033[36m=\033[m'*100)
print('\nInforme valores ao computador. ao final do processo, será apresentada a média, maior e menor valor.')
continuar = 'S'
cont = maior = menor = soma = media = 0
while continuar in 'S':
    n = int(input('Digite um valor: '))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    continuar = str(input('\nVocê deseja acrescentar mais valores? [S/N] - ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('\nOpção inválida. Você deseja acrescentar mais valores? [S/N] - ')).upper().strip()[0]
media = soma / cont
print()
print('Foram digitados {} valor(es). A média entre todos os valores digitados é igual a {:.2f} '.format(cont, media))
print('O maior número digitado é [{}] e o menor é [{}]'.format(maior, menor))
