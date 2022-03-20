"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
30% do salário ou então o empréstimo será negado.
"""

from time import sleep

print('\033[33m-=-\033[m' * 30)
print('{:^90}'.format('FINANCIAMENTO CASA PRÓPRIA'))
print('\033[33m-=-\033[m' * 30)
print()
valor = float(input('Digite o valor do imóvel: R$ '))
salario = float(input('Informe o salário do comprador: R$ '))
ano = int(input('Em quantos anos o financiamento será parcelado? '))
parcela = valor / (ano * 12)
print()
print('\033[33m-=-\033[m' * 30)
print()
print('CALCULANDO', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print()
if parcela > (salario * 0.3):
    print('O financiamento não foi aprovado. O valor da prestação, que é de R$ {:.2f},\né superior a 30% do '
          'salário do comprador.'.format(parcela))
else:
    print('Financiamento aprovado.')
print()
print('\033[33m-=-\033[m' * 30)
print()
print('{:^90}'.format('TENHA UM BOM DIA'))
