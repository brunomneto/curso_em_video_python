"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.
"""
print()
print('\033[36m=\033[m'*50)
print('{:^50}'.format('PROGRESSÃO ARITMÉTICA'))
print('\033[36m=\033[m'*50)
print()
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print()
print('Os dez primeiros termos da PA são os seguintes:')
for c in range(0, 10):
    print('{}'.format(n1), end=' > ')
    n1 += r
print('FIM!')
