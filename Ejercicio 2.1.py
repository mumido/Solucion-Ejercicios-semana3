#EJERCIOCIO 2.1

capital = float (input("Ingresar cantidad que se desea invertir en $ARS: ") )

x = int (input("Ingresar tasa de interés anual %: "))
n = int (input("Ingresar cantidad de años: "))

Cn = capital * (1 + x/100) ** n

print ("Monto final a obtener: $ " +str(Cn))
