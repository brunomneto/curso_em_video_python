"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
print()
print('=-' * 40)
print('{:^80}'.format('CADASTRAMENTO DE PÚBLICO'))
print('=-' * 40)
idade = maior = homens = mulheres = 0
sexo = continuar = ' '
while True:
    print('\n--CADASTRO--')
    idade = int(input('Informe a idade da pessoa: '))
    while idade < 0:
        idade = int(input('Informação inválida. Informe a idade da pessoa: '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Por favor, informe o sexo da pessoa [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Informação inválida. Informe o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = str(input('Você deseja cadastrar mais um pessoa? [S/N] - ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Quer cadastrar outra pessoa? [S/N] - ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nCom os dados cadastrados, encontramos {maior} pessoas maiores de 18 anos.')
print(f'Além disso, contabilizamos {homens} homens cadastrados, além de {mulheres} mulheres com menos de 20 anos.')
