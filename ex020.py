import random
a1 = input('Digite o nome do primeiro aluno: ')
print('')
a2 = input('Digite o nome do segundo aluno: ')
print('')
a3 = input('Digite o nome do terceiro aluno: ')
print('')
a4 = input('Digite o nome do quarto aluno: ')
lista = '{} {} {} {}'.format(a1, a2, a3, a4).split()
random.shuffle(lista)
print('')
print('A ordem de apresentação dos trabalhos é: {}'.format(lista))
