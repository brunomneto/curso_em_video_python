"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
nome = ['nome0', 'nome1', 'nome2', 'nome3']
idade = ['idade0', 'idade1', 'idade2', 'idade3']
sexo = ['sexo0', 'sexo1', 'sexo2', 'sexo3']
homem = 0
idademaisvelho = 0
idmaisvelho = 0
mulher = 0
mmv = 0
print('='*50)
print('{:^50}'.format('LISTA DE PESSOAS'))
print('='*50)
print()
for c in range(0, 4):
    nome[c] = str(input('Digite o nome da {}ª pessoa: '.format(c + 1))).strip()
    idade[c] = int(input('Digite a idade da {}ª pessoa: '.format(c + 1)))
    sexo[c] = str(input('Qual é o sexo da {}ª pessoa (M/F): '.format(c + 1)).upper())
    if sexo[c] == 'M':
        homem += 1
        if idade[c] > idademaisvelho:
            idademaisvelho = idade[c]
            idmaisvelho = c
    elif sexo[c] == 'F':
        mulher += 1
        if idade[c] < 20:
            mmv += 1
    print('-'*50)

print('Cadastro finalizado.')
print()
print('='*50)
print()
m = (idade[0] + idade[1] + idade[2] + idade[3]) / 4
print('A média de idade do grupo é igual a {:.1f}.'.format(float(m)))
if homem == 0:
    print('Não existem homens na lista.')
else:
    print('O nome do homem mais velho é {}.'.format(nome[idmaisvelho]))
if mulher == 0:
    print('Não existem mulheres na lista.')
elif mulher > 0 and mmv == 0:
    print('Nenhuma mulher da lista possui menos de 20 anos.')
elif mulher > 0 and mmv == 1:
    print('Apenas uma mulher na lista possui menos de 20 anos.')
elif mulher > 0 and mmv > 1:
    print('Existem {} mulheres com menos de 20 anos.'.format(mmv))
