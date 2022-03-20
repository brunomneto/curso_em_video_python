"""
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
print()
print('\033[1;33m-=-\033[m' * 30)
salario = float(input('Digite o salário do funcionário: \033[32mR$\033[m '))
print('\033[33m-=-\033[m' * 30)
if salario <= 1250:
    salario = salario + (salario * 0.15)
    print('O salário do funcionário terá aumento de 15% e será igual a \033[32mR$ {:.2f}\033[m .'.format(salario))
else:
    salario = salario + (salario * 0.10)
    print('O salário do funcionário terá aumento de 10% e será igual a \033[32mR$ {:.2f}\033[m .'.format(salario))
print('\033[33m-=-\033[m' * 30)