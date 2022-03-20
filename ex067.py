"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
print()
print('TABUADA ELETRÔNICA')
print()

while True:
    print('-=-' * 20)
    n = int(input('Você gostaria de ver a tabuada de qual número? '))
    if n < 0:
        print('\nFINALIZANDO...')
        break
    else:
        for c in range(1, 11):
            r = n * c
            print(f'{c:2} X {n} = {r}')
