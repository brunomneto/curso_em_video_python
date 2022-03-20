print(50*'=')
print('              Calculadora de Médias        ')
print(50*'=')
nome = input(' Nome do(a) aluno(a): ')
n1 = float(input(' Digite a primeira nota do(a) aluno(a): '))
n2 = float(input(' Digite a segunda nota: '))
m = (n1+n2)/2
print(50*'=')
print(' A média do(a) aluno(a) {} é {:.2f}'.format(nome, m))

