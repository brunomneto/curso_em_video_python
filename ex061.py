"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print()
print('\033[36m=\033[m'*50)
print('{:^50}'.format('PROGRESSÃO ARITMÉTICA 2.0'))
print('\033[36m=\033[m'*50)
print()
c = 0
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
print('\nOs dez primeiros termos da PA são os seguintes: ')
while c < 10:
    print('[{}] '.format(n1), end='')
    n1 += r
    c += 1
print()
