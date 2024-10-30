'''
EJERCICIO 5: Reescribe tu cálculo de pago (EJERCICIO 2) para darle al empleado 1.5 veces la tarifa 
por hora por las horas trabajadas por encima de las 40 horas. La salida es la siguiente:
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

print ("Programa Horas/Tarifas")
print ("----------------------")
horas = int(input("Por favor, introduce las horas: "))
tarifa = int(input("Por favor, introduce el precio de la tarifa por cada horas: "))
if horas>40 :
    print ("El coste es de : " + str(horas * tarifa * 1.5) + "€")
else :
    print ("El coste es de: " + str(horas * tarifa) + "€")