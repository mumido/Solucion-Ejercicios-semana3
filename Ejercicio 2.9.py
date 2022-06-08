#Ejercicio 2.9.

number = int(input("Escribe un entero positivo: "))

for i in range(0, number):
    if i % 2 != 0:
        print(i, end=", ")
