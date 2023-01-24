print('João pescador')
print('peso(50kg) do peixe no estado SP, tendo como valor de multa R$4,00 de kg excedente')
peso = float(input('Digite o peso do peixe comprado: '))
if peso > 50:
    excesso = peso - 50
print (excesso)
multa = excesso * 4
print('Valor da multa é: ',multa)
