""""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
print()
print('\033[36m=\033[m'*50)
print('{:^50}'.format('PROGRESSÃO ARITMÉTICA 3.0'))
print('\033[36m=\033[m'*50)
print()
c = 0  # contador para exibição de termos da PA. Limitado por k.
k = 10  # número de elementos da PA que serão exibidos. Começa em dez porque é o pedido. Muda a cada ciclo de exibição.
total = 0
n1 = int(input('Digite o primeiro termo da PA: '))  # primeiro termo da PA.
r = int(input('Informe a razão da PA: '))  # razão da PA.
print('\nOs dez primeiros termos da PA são os seguintes: ')
while k > 0:  # enquanto o número de elementos a serem exibidos no próximo ciclo for maior que zero, segue o laço.
    total += k
    while c < k:
        print('[{}] '.format(n1), end='')
        n1 += r
        c += 1
    k = int(input('\n\nVocê quer mostrar mais quantos termos da PA? '))
    if k > 0:  # se o número de termos a serem exibidos no próximo ciclo for maior que zero, o contador é zerado.
        c = 0
print('\nAcabou! Foram exibidos {} termos da PA'.format(total))
