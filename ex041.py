"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
from datetime import date

print('\033[33m-*-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('CONFEDERAÇÃO NACIONAL DE NATAÇÃO - CATEGORIAS'))
print('\033[33m-*-\033[m' * 30)
print()
print('\033[37m---------- CATEGORIAS DE NATAÇÃO ----------\033[m')
print('{}'.format('\033[36mMIRIM\033[m - Até 9 anos'))
print('{}'.format('\033[33mINFANTIL\033[m - Até 14 anos'))
print('{}'.format('\033[32mJUNIOR\033[m - Até 19 anos'))
print('{}'.format('\033[34mSÊNIOR\033[m - Até 20 anos'))
print('{}'.format('\033[31mMASTER\033[m - Acima de 20 anos'))
print('\033[37m-------------------------------------------\033[m')
print()
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano
print()
if 0 < idade <= 9:
    print('O atleta tem {} anos, e pertence à categoria \033[36mMIRIM\033[m.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos, e pertence à categoria \033[33mINFANTIL\033[m.'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos, e pertence à categoria \033[32mJUNIOR\033[m.'.format(idade))
elif 19 < idade <= 25:
    print('O atleta tem {} anos, e  pertence à categoria \033[34mSÊNIOR\033[m.'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos, e pertence à categoria \033[31mMASTER\033[m.'.format(idade))
else:
    print('ERRO: IDADE INVÁLIDA')
print()
print('\033[33m-*-\033[m' * 30)


