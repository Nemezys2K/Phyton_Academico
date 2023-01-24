print('Salário do trabalhado')
salarioBrut = float(input('Digite o seu salário ganho por mês em R$: '))
print('Meu salário bruto é..',salarioBrut)
print('IR..(imposto de renda é 11%)')
ir = salarioBrut * (11/100)
resIr = salarioBrut - ir
print(resIr)
print('INSS..(imposto 8%)')
inss = salarioBrut * (8/100)
resInss = salarioBrut - inss
print(resInss)
print('Sindicato..(imposto 5%)')
sind = salarioBrut * (5/100)
resSind = salarioBrut - sind
print(resSind)
s = salarioBrut *(24/100)
resS = salarioBrut - s
print('O valor total e..Salario bruto R$:',salarioBrut,' de acordo com imposto feitos então salário liqquido e R$: ',resS) 



