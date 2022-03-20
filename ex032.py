"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date
from time import sleep

separador = '\033[1;33m-=-\033[m' * 35
print()
print(separador)
ano = int(input('Digite um ano para saber se ele é bissexto. Se quiser escolher o ano atual, digite 0 >>> '))
print(separador)
print('PROCESSANDO...')
sleep(3)
print(separador)
"""if ano % 400 == 0:
    print('O ano {} É bissexto.'.format(ano))
else:
    if ano % 4 == 0:
        if ano % 100 != 0:
            print('O ano {} É bissexto.'.format(ano))
    else:
        print('O ano {} NÃO é bissexto.'.format(ano))
"""
if ano == 0:
    ano = date.today().year  # pega o ano atual configurado na máquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[1;32mÉ\033[m bissexto.'.format(ano))
else:
    print('O ano {} \033[1;31mNÃO É\033[m bissexto.'.format(ano))
print(separador)
