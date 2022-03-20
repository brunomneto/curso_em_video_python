"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta
viagens mais longas.
"""
km = float(input('\033[4;34mQual é a distância em km a ser percorrida na viagem?\033[m '))
print()
if km <= 200:
    print('\033[35mO valor cobrado pela viagem será de R$ {:.2f} .\033[m'.format(km * 0.5))
else:
    print('\033[35mO valor cobrado pela viagem será de R$ {:.2f} .\033[m'.format(km * 0.45))
