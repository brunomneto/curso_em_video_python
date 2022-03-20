"""Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando
 em seguida o primeiro e o último nome separadamente."""

print()
nomecompleto = str(input('Digite seu nome \033[4mcompleto\033[m: ')).strip().split()
numnome = len(nomecompleto)
print()
print('\033[1;35mPrimeiro nome:\033[m {}'.format(nomecompleto[0]))
print('\033[1;31mÚltimo nome:\033[m {}'.format(nomecompleto[numnome - 1]))
