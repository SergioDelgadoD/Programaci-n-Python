'''
EJERCICIO 6: Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" 
para que su programa maneje la entrada no numérica correctamente imprimiendo un mensaje y saliendo del programa. 
A continuación se muestran una ejecución del programa:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
'''
print ("Programa Horas/Tarifas")
print ("----------------------")

try:
    horas = int(input("Por favor, introduce las horas: "))
    tarifa = int(input("Por favor, introduce el precio de la tarifa por cada horas: "))

except ValueError:
	print ("Error, please enter numeric input")
    
else:
    print ("El coste es de: " + str(horas * tarifa) + "€")