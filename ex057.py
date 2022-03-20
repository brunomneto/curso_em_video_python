"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

nome = str(input('Olá, qual é o seu nome? ')).strip()
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Opção inválida, tente novamente. Informe seu sexo (M/F): ')).strip().upper()
print('\nO seu nome é {} e seu sexo é [{}]'.format(nome, sexo))
