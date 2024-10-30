'''
EJERCICIO 8: Reescribe su cálculo de pago (EJERCICIO 2) con tiempo y medio para horas extras 
y crea una función llamada "computepay" que tome dos parámetros ("hours" y "rate").
'''

print ("Programa Horas/Tarifas")
print ("----------------------")

def computepay():
    hours = int(input("Por favor, introduce las horas: "))
    rate = int(input("Por favor, introduce el precio de la tarifa por cada horas: "))
    return hours, rate

horas, tarifa = computepay()

print ("El coste es de : " + str(horas * tarifa) + "€")