print('Calculadora de Tinta')
a = float(input('Diga a altura em metros da parede: '))
l = float(input('Agora diga a largura, em metros: '))
area = a * l
print('')
print('A área total da sua parede é de {:.2f}m² e serão necessários {:.2f} litro(s) de tinta para pintá-la.'.format(area, (area/2)))
