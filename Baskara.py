print("Exercicios 1")

a = float(input("valor de A: "))
b = float(input("valor de B: "))
c = float(input("valor de C: "))


def baskara(a,b):
    delta = b**2 - 4*a*c
    x1 = (-1*b + delta)/2*a
    x2 = (-1*b - delta)/2*a
    return [x1,x2];
    

vari = baskara(a,b)  
print("O valor  de X1 e X2: ",vari) 