print('A conta de telefone com três faixa de preço')
minutos = int(input('Quantos minutos foram utilizados no mês: '))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print('Você vai pagar este mês: R$ ',minutos)
