from unittest import case


n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro núemro: "))

print("O tripo do 1º é: ",n1*3)
print("O tripo do 2º é: ",n2*3)
print("O tripo do 3º é: ",n3*3)

def calculus(num1,num2,num3):
    while True:
        if n1 > -999:
            print("O valor é valido..")
        elif n2 > -999:
            print("O valor ainda é valido..")
        else:
            print("Fim do programa..")
        return

calculus(n1,n2,n3)
