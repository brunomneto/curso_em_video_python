"""Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome."""

titulo = 'DETECTOR DE SILVAS'
print('-'*75)
print('{:^75}'.format(titulo))
print('-'*75)
print()
nome = str(input('Digite o nome completo da pessoa escolhida: '))
print()
nomecompleto = nome.upper().strip().split()
print('O resultado do teste para detectar um Silva é: {}!'.format('SILVA' in nomecompleto))
