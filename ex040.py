"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""
print('\033[33m-=-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('Calculadora de Médias'))
print('\033[33m-=-\033[m' * 30)
print()
n1 = float(input('Digite a N1 do aluno: '))
n2 = float(input('Digite a N2: '))
print()
print('\033[33m-=-\033[m' * 30)
print()
m = (n1 + n2) / 2
if m < 5:
    print('A média das notas é {:.1f} - O aluno foi \033[31mREPROVADO\033[m.'.format(m))
elif 5 <= m < 7:
    print('A média das notas é {:.1f} - O aluno está em \033[33mRECUPERAÇÃO\033[m.'.format(m))
else:
    print('A média das notas é {:.1f} - O aluno está \033[32mAPROVADO\033[m'.format(m))
print()
