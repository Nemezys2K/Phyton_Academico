print('Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58')
alt = float(input('Digite a altura da pessoa: '))
pes = float(input('Digite o peso da pessoa: '))
resultado = (pes/(alt**2))
print('O resultado  é.. ', resultado,' Então pelo IMC seu peso é. ')
if resultado <= 15.9:
    print('Você está, bem abaixo do peso de acordo com IMC..')
elif resultado >= 16 and resultado <= 19.9:
    print('Você está a baixo do peso ideial de acordo com IMC..')
elif resultado >= 20 and resultado <= 24.9:
    print('Você está com peso ideal de acordo com IMC..')
elif resultado >= 25 and resultado <= 29.9:
    print('Você está com sobrepeso de acordo com IMC..')
elif resultado >= 30 and resultado <= 39.9:
    print('Você está com obesidade de acordo com IMC..')
elif resultado >= 40:
    print('Você está com obesidade morbida de acordo com IMC..')
    print('De acordo com os calculos feitos com formula do IMC = (peso KG / altura **2)')

