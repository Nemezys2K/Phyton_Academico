contador = 1
resposta = 'sim'
while (resposta == 'sim' or resposta == 's'):
    x = int(input('Digite o valor: '))
    r = x * 3
    print('O valor é: ',r)
    resposta = input('Deseja continuar: ')
