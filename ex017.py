import math
cato = float(input('Digite o valor do cateto oposto do triângulo: '))
print('')
cata = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(cato, cata)
print('')
print('A hipotenusa do triângulo tem valor igual a {:.2f}'.format(hip))
