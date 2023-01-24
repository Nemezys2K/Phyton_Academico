print('Fazer um programa que leia um número e exiba a ordem de grandeza seguindo a tabela abaixo')
x = int(input('Digite o valor: '))
if x >= 0 and x < 100:
    print(f'X entre 0 e 100 o valor:{x:2.1f}')
elif x >= 100 and x <1000:
    print(f'X entre 100 e 1000 o valor:{x:2.1f}')
elif x >= 1000:
    print(f'X maior igual ou a 1000 o valor:{x:2.1f}')
elif x < 0:
    print(f'X e menor que 0 o valor:{x:2.1f}')
else:
    print('Tabela de supeioridade númerico')
