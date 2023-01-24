print('Escreva um programa que corrija um teste de múltiplas escolhas, mostrando a quantidade de acertos, contendo três questões, cada')
print('questão possui 5 alternativas do tipo a, b, c, d e e. A resposta correta da primeira questão é “b”; da segunda, “a”; e da terceira, “d”.')
print('O programa conta um ponto a cada resposta correta. Considere a possibilidade do programa aceitar respostas com letra maiúsculas')
print('e minúsculas em todas as questões.')
contAceto = 0
resp1 = input('Digite a primeia resposta ceta a, b, c, d ou e : ')
if resp1 == 'b' or resp1 == 'B':
   contAceto += 1
resp2 = input('Digite a segunda resposta ceta a, b, c, d ou e : ')
if resp2 == 'a' or resp2 == 'A':
   contAceto += 1
resp3 = input('Digite a terceira resposta ceta a, b, c, d ou e : ')
if resp3 == 'd' or resp3 == 'D':
    contAceto += 1
print( "voçe acetou " + str(contAceto))
