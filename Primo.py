print("Escribe un número:")
numero = int(input())
n = numero-1
x = 0
while n>1:
    if(numero%n == 0):
        print("no es primo")
        x=x+1
        break
    n=n-1

if(x==0):
    print("es primo")
