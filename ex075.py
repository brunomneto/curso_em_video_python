"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

tupla = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite outro número: ')),
         int(input('Digite o último número: ')))

print(f'\nOs números digitados foram: {tupla}.')

if tupla.count(9) == 1:
    print(f'O número 9 foi digitado {tupla.count(9)} vez.')
else:
    print(f'O número 9 foi digitado {tupla.count(9)} vezes.')

if tupla.count(3) == 0:
    print('O número 3 não foi digitado nenhuma vez.')
else:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3) + 1}ª posição.')

print('Os valores pares digitados são:')
for c in tupla:
    if c % 2 == 0:
        print(f'-> {c}')
