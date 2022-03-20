"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('\nDigite um número entre 0 e 20: '))
    while not 0 <= n <= 20:
        n = int(input('Valor inválido. Digite novamente um valor entre 0 e 20: '))
    print(f'Você digitou o número {ext[n]}.')
    continua = str(input('\nVocê deseja continuar? [S/N] - ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Opção Inválida. Você deseja continuar? [S/N] - ')).strip().upper()[0]
    if continua == 'N':
        break
