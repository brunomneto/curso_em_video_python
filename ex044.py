"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""
print('\033[33m-*-\033[m' * 30)
print('\033[35m{:^90}\033[m'.format('LOJA DO SEU ZÉ'))
print('\033[33m-*-\033[m' * 30)
print()
preco = float(input('Valor total da compra: R$ '))
print()
print('\033[37m------------- FORMAS DE PAGAMENTO -------------\033[m')
print('{}'.format('(1) - À Vista em dinheiro (10% de desconto)'))
print('{}'.format('(2) - À Vista no cartão (5% de desconto)'))
print('{}'.format('(3) - Até 2x no cartão (s/ juros)'))
print('{}'.format('(4) - Até 12x no cartão (c/ juros 20%)'))
print('\033[37m-----------------------------------------------\033[m')
pag = int(input('Selecione a forma de pagamento: '))
if pag == 1:
    print('Valor a pagar em dinheiro: R$ {:.2f}'.format(preco - (preco * 0.1)))
elif pag == 2:
    print('Valor à vista no cartão: R$ {:.2f}'.format(preco - (preco * 0.05)))
elif pag == 3:
    duasvezes = preco / 2
    print('Valor até 2x no cartão: R$ {:.2f} em 2 parcelas de R$ {:.2f}'.format(preco, duasvezes))
elif pag == 4:
    print('Valor até 12x no cartão: R$ {:.2f}'.format(preco + (preco * 0.2)))
    nparcelas = int(input('Digite o número de parcelas: '))
    parcela = (preco + (preco * 0.2)) / nparcelas
    print('O pagamento será realizado em {} parcelas de R$ {:.2f}'.format(nparcelas, parcela))
else:
    print('\033[31mOpção Inválida\033[m')
print('\033[37m-----------------------------------------------\033[m')