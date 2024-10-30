'''
EJERCICIO 7: Escribe un programa para solicitar una puntuación entre 0.0 y 1.0. 
Si la puntuación está fuera de rango, imprime un mensaje de error. Si la puntuación está entre 0.0 y 1.0, 
imprime una calificación usando la siguiente tabla:
Score	Grade
>= 0.9	A
>= 0.8	B
>= 0.7	C
>= 0.6	D
< 0.6	F
Ejecute el programa repetidamente para probar los diferentes valores de entrada.
'''
print ("Programa solicitar puntuación entre 0.0 y 1.0")
print ("---------------------------------------------")

def my_puntuacion():
    return float(input("Por favor, introduce puntuación entre 0.0 y 1.0: "))

pun = my_puntuacion()

if  pun < 0.0 or pun > 1.0:
	print ("Error, por favor ha de introducir un número entre 0.0 y 1.0")
     
elif pun >= 0.9:
    print ("Su calificación es de A")

elif pun >= 0.8:
    print ("Su calificación es de B")

elif pun >= 0.7:
    print ("Su calificación es de C")

elif pun >= 0.6:
    print ("Su calificación es de D")

else:
    print ("Su calificación es de F")