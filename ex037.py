"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

print('\033[33m-=-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('CONVERSOR DE BASES'))
print('\033[33m-=-\033[m' * 30)
print()
num = int(input('Digite um número inteiro, base decimal: '))
print()
print('Escolha a base numérica para conversão:\n\n1 - Binário\n2 - Octal\n3 - Hexadecimal')
print()
opcao = int(input('Digite a opção: '))
print()
if opcao == 1:
    print('O número {} em base binária é igual a {} .'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em base octal é igual a por {} .'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em base hexadecimal é igual a {} . '.format(num, hex(num)[2:]))
else:
    print('ERRO.')
print('')
