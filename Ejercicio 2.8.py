#Ejercicio 2.8.

n = int(input("Escribe un entero positivo: "))

for i in range(n, -1, -1):
    if i >= 0:
        print(i, end=",")

