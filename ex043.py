"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""
print('\033[33m-*-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('CÁLCULO IMC - ÍNDICE DE MASSA CORPORAL'))
print('\033[33m-*-\033[m' * 30)
print()
print('Para o cáluclo de IMC precisamos do seu peso e da sua altura.')
peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Agora forneça a sua altura, em metros: '))
print()
print('\033[33m-*-\033[m' * 30)
print()
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Seu IMC está abaixo de 18.5 - Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Seu IMC está entre 18.5 e 25 - Peso ideal')
elif 25 <= imc < 30:
    print('Seu IMC está entre 25 e 30 - Sobrepeso')
elif 30 <= imc < 40:
    print('Seu IMC está entre 30 e 40 - Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
print()
print('\033[33m-*-\033[m' * 30)
