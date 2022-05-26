#Ej. 7

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (mts): "))

imc = peso / (altura**altura)

print ("Tu índice de masa corporal es:", end=" ")
print((round(imc, 2)))
