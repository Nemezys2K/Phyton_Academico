print('Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. ')
print('Calcule o preço da passagem, cobrando. R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas')
dist = float(input('Digite a distância a percorrer: '))
if dist <= 200:
    pas = 0.5 * dist
else:
    pas = 0.45 * dist
print(f'O preço da passagem: R${pas:7.2f}')
