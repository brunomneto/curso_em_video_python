"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo.
"""
print()
a = int(input('\033[34mDigite a medida do segmento de reta A:\033[m '))
b = int(input('\033[33mDigite a medida do segmento de reta B:\033[m '))
c = int(input('\033[32mDigite a medida do segmento de reta C:\033[m '))
print()
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos de retas de medidas \033[34m{}\033[m, \033[33m{}\033[m e \033[32m{}\033[m podem formar um'
          ' triângulo.'.format(a, b, c))
else:
    print('Os segmentos de retas de medidas \033[34m{}\033[m, \033[33m{}\033[m e \033[32m{}\033[m \033[31mNÃO\033[m '
          'podem formar um triângulo.'.format(a, b, c))
