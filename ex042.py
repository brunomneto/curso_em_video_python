"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""
print()
a = float(input('\033[34mDigite a medida do segmento de reta A:\033[m '))
b = float(input('\033[33mDigite a medida do segmento de reta B:\033[m '))
c = float(input('\033[32mDigite a medida do segmento de reta C:\033[m '))
print()
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos de retas de medidas \033[34m{:.2f}\033[m, \033[33m{:.2f}\033[m e \033[32m{:.2f}\033[m podem'
          ' formar um triângulo.'.format(a, b, c))
    if a == b == c:
        print('Este triângulo é do tipo \033[35mEQUILÁTERO\033[m: todos os lados iguais.')
    elif a != b != c != a:
        print('Este triângulo é do tipo \033[31mESCALENO\033[m: todos os lados diferentes.')
    elif a == b != c or a == c != b or a != b == c:  # será que abrnge todas as possibilidades? Não é melhor usar else?
        print('Este triângulo é do tipo \033[36mISÓCELES\033[m: dois lados iguais, um diferente.')

else:
    print('Os segmentos de retas de medidas \033[34m{:.2f}\033[m, \033[33m{:.2f}\033[m e \033[32m{:.2f}\033[m '
          '\033[31mNÃO\033[m podem formar um triângulo.'.format(a, b, c))
print()
