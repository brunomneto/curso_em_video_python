"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

print(50*'\033[32m=\033[m')
print('{:^50}'.format(' TABUADA ELETRÔNICA v2.0 '))
print(50*'\033[32m=\033[m')
print()
n = int(input('Você quer saber a tabuada de qual número? '))
print()
for c in range(1, 11):
    print(' {:2} X {} = {:2} '.format(c, n, c * n))
print()
