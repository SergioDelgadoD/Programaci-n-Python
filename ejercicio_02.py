#EJERCICIO 2: Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.

print ("Programa Horas/Tarifas")
horas = int(input("Por favor, introduce las horas: "))
tarifa = int(input("Por favor, introduce el precio de la tarifa por cada horas: "))
print ("El coste es de : " + str(horas * tarifa) + "€")