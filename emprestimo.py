print('Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.')
print('O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.')
print('O valor da prestação mensal não pode ser superior a 30% do salário')
print(' Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar.')
valC = float(input('Digite o valor pago na casa a venda: '))
sal = float(input('Digite o salário R$: '))
qntPag = int(input('Quantos anos a pagar: '))
meses = qntPag * 12
prestacao = valC / meses
if prestacao > sal * 0.3:
    print('Infelizmente você não pode obter o empréstimo')
else:
    print(f'Valor da prestacao: R${prestacao:7.2f} Emprestimo esta OK!')

