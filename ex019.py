import random
a1 = input('Digite o nome do primeiro aluno: ')
print('')
a2 = input('Digite o nome do segundo aluno: ')
print('')
a3 = input('Digite o nome do terceiro aluno: ')
print('')
a4 = input('Digite o nome do quarto aluno: ')
print('')
print('O aluno(a) {} foi sorteado para apagar o quadro essa semana!'.format(random.choice([a1, a2, a3, a4])))