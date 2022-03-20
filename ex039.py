"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

print('\033[33m-=-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('ALISTAMENTO MILITAR'))
print('\033[33m-=-\033[m' * 30)
print()
nome = str(input('Digite seu nome: '))
nasc = int(input('Digite o seu ano de nascimento: '))
print()
idade = date.today().year - nasc
if idade < 18:
    print('{}, você não está no período de alistamento. Falta(m) {} ano(s) para chegar a sua vez!'
          .format(nome, (18 - idade)))
elif idade > 18:
    print('{}, você perdeu o período de alistamento militar e está {} ano(s) atrasado. Regularize sua situação.'
          .format(nome, (idade - 18)))
else:
    print('{}, este é o momento de realizar o seu alistamento militar. Vá até o local indicado.'.format(nome))
