"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = list()
print()
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
print('=' * 50)
print(f'Você digitou os seguintes valores: {valores}\n')
print(f'O maior valor é {max(valores)} e aparece nas posições ', end='')
for c in range(0, 5):
    if valores[c] == max(valores):
        print(c, end='... ')
print(f'\nO menor valor é {min(valores)} e aparece nas posições ', end='')
for c in range(0, 5):
    if valores[c] == min(valores):
        print(c, end='... ')
print()
