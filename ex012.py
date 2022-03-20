print('Dia de oferta e descontos!')
preco = float(input('Digite o preço do produto: '))
novopreco = preco - (preco*0.05)
print('O produto escolhido custa R$ {:.2f}, mas com o nosso desconto especial de 5% fica por R$ {:.2f}! '.format(preco, novopreco))
