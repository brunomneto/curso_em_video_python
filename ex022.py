"""Exercício Python 22:

Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""


nomecompleto = input('Digite seu nome completo: ')
cadanome = nomecompleto.strip().split()
print()
print('O seu nome com todas as letras maiúsculas é "{}".'.format(nomecompleto.upper()))
print('O seu nome com todas as letras minúsculas é "{}".'.format(nomecompleto.lower()))
print('O seu nome completo possui {} letras.'.format(len(''.join(cadanome))))
print('O seu primeiro nome possui {} letras.'.format(len(cadanome[0])))
