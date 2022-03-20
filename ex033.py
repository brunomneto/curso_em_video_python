"""
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
print()
a = int(input('\033[32mDigite um número:\033[m '))
b = int(input('\033[36mDigite mais um número:\033[m '))
c = int(input('\033[34mDigite um terceiro número:\033[m '))
print()
"""
if n1 < n2:
    menor = n1
    maior = n2
    if n1 < n3:
        menor = n1
        if n2 < n3:
            maior = n3
        else:
            maior = n2
    else:
        menor = n3
else:
    maior = n1
    menor = n2
    if n2 < n3:
        menor = n2
        if n1 < n3:
            maior = n3
        else:
            maior = n1
    else:
        menor = n3
"""

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('>>> \033[1;35m{}\033[m é o \033[35mmenor\033[m número <<<'.format(menor))
print('>>> \033[1;31m{}\033[m é o \033[31mmaior\033[m número <<<'.format(maior))
