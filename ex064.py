"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).
"""
print()
print('\033[36m=\033[m'*90)
print('{:^90}'.format('SOMA DE NÚMEROS'))
print('\033[36m=\033[m'*90)
print('\nO programa irá somar todos os valores digitados e informar no fim o valor da soma e quantos números somados.')
print('Digite 999 para encerrar o processo.\n')
n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n > 999:
        print('Valor Inválido')
    elif n == 999:
        print('\nFim!')
    else:
        soma += n
        cont += 1
print('A soma dos {} números digitados é igual a {}.'.format(cont, soma))
