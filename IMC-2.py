print('Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas')
nome = str(input('Digite o nome do homem ou da mulher: '))
alt = float(input('Digite a altura da pessoa: '))
pes = float(input('Digite o peso da pessoa: '))
print('Altura do(a) ',nome,' é ', alt,' com o peso de ',pes,'Kg')
resM = (pes/alt**2) + 0.01
print('O resultado do indice caso se for peso do homem é: ',resM)
resF = (pes/alt**2) - 0.01
print('O resultado do indice caso se for peso de mulher é: ',resF)
#a partir daqui é mostrado indice do homem#
if resM >= 20 and resM <= 24.9:
    print('Se caso se indice apareca entre 20 a 24.9',resM,' seu peso e ideal.. se caso não for..')
elif resM <= 16 and resM >= 19.9:
    print('Então está a baixo do peso ideal para homem..')
elif resM >= 25 and resM <= 30:
    print('Se caso esteja entre 25 a 40 esta com sobre peso a obesidade ',resM)
elif resM > 40:
    print('se for acima de 40 o indice então e obesidade morbida ')
#a partir daqui é mostrado indice da mulher#    
elif resF >= 20 and resF <= 24.9:
    print('Se caso se indice apareca entre 20 a 24.9',resF,' seu peso e ideal.. se caso não for..')
elif resF <= 16 and resF >= 19.9:
    print('Então está a baixo do peso ideal para homem..')
elif resF >= 25 and resF <= 30 :
    print('Se caso esteja entre 25 a 40 esta com sobre peso a obesidade ',resF)
elif resM > 40:
    print('se for acima de 40 o indice então e obesidade morbida ')



