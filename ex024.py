"""Exercício Python 24: Crie um programa que leia o nome de uma cidade
 e diga se ela começa ou não com o nome “SANTO”."""

nome = str(input('Qual é o nome da sua cidade? ')).upper().split()
print('É {} que o nome da sua cidade começa com a palavra "Santo".'.format(nome[0] == 'SANTO'))
