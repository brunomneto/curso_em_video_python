import math
ang = float(input('Digite o valor do ângulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('')
print('Para o ângulo de {}°, o seno vale {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(ang, sen, cos, tan))
