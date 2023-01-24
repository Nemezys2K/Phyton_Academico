def valores(x,y):
    if x > y:
        return x
    else:
        return y

resultado = int(input("Digitando o valor: "))
result = int(input("Digitando mais um valor: "))

print("O valor digitado: ",valores(resultado,result))