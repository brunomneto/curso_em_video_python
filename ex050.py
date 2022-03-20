"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
print()
print('\033[36m=\033[m'*50)
print('{:^50}'.format('SOMA DE PARES'))
print('\033[36m=\033[m'*50)
print()
somapar = 0
contapar = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        contapar += 1
        somapar += n
print()
if contapar == 1:
    print('Você digitou {} número par e a soma dos pares é igual a {}.'.format(contapar, somapar))
else:
    print('Você digitou {} números pares e a soma deles é igual a {}.'.format(contapar, somapar))
