#Ejercicio 2.7.

number_one = int(input("Escribe el primer número: "))
number_two = int(input("Escribe el segundo número: "))


for i in range(number_one, number_two):
    if i % 2 == 0:
        print(i)
