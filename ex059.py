"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

print('\033[33m-=-\033[m'*20)
print('{:^60}'.format('CALCULADORA ESPECIAL'))
print('\033[33m-=-\033[m'*20)
print()

menu = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Agora digite outro número: '))

print()
while menu != 5:
    print('\033[33m-=-\033[m' * 20)
    print('Qual operação você quer realizar com {} e {}?'.format(n1, n2))
    print('[1] Soma\n[2] Multiplicação\n[3] Maior valor\n[4] Escolher novos valores\n[5] Sair')
    menu = int(input('Realizar a opção: '))
    if menu < 1 or menu > 5:
        print('\nOpção inválida. Escolha novamente.\n')
    elif menu == 1:
        soma = n1 + n2
        print('\nSOMA: {} + {} = {} \n'.format(n1, n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print('\nMULTIPLICAÇÃO: {} X {} = {} \n'.format(n1, n2, mult))
    elif menu == 3:
        if n1 == n2:
            print('\nOs números {} e {} são iguais.\n'.format(n1, n2))
        elif n1 > n2:
            maior = n1
            print('\nO maior valor é {} \n'.format(maior))
        else:
            maior = n2
            print('\nO maior valor é {} \n'.format(maior))
    elif menu == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Agora digite outro número: '))
        print()
    elif menu == 5:
        print()
        print('\033[33m-=-\033[m' * 20)
        print('\nOPERAÇÃO FINALIZADA')
    sleep(2)
