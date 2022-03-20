"""Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""
print()
frase = input('Digite uma frase: ')
print()
frase = frase.upper().strip()
frase = frase.replace('Á', 'A').replace('À', 'A').replace('Ã', 'A').replace('Â', 'A')
#frase = frase.replace('À', 'A')
#frase = frase.replace('Ã', 'A')
#frase = frase.replace('Â', 'A')
print('\033[33mA frase digitada apresenta \033[m\033[32m{}\033[m\033[33m letra(s) "A".\033[m '.format(frase.count('A')))
print('\033[33mA primeira ocorrência de "A" se dá na posição\033[m\033[32m {}\033[m\033[33m.\033[m'.format(frase.find('A')+1))
print('\033[33mA última ocorrência de "A" se dá na posição\033[m\033[32m {}\033[m\033[33m.\033[m'.format(frase.rfind('A')+1))
