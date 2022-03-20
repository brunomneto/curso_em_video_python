"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
print()
v = float(input('Digite a velocidade do carro em km/h: '))
print()
if v > 80:
    print('\033[31mCarro acima do limite de velocidade. Valor da multa aplicada: R$ {:.2f}.\033[m'.format((v - 80)*7))
else:
    print('\033[32mCarro dentro do limite de velocidade. Boa viagem.\033[m')
