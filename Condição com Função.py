def multiplos(x,y):
    if x % y == 0:
        return True
    else:
        return False

valorX = int(input("Digite um valor: "))
valorY = int(input("Digite outro valor: "))
print("O maior valor é: ",multiplos(valorX,valorY))