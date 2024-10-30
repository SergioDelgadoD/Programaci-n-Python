'''
EJERCICIO 9: Reescribe el programa de calificación del capítulo anterior (EJERCICIO 7)
utilizando una función llamada "computegrade" que tome una puntuación como parámetro y devuelva una nota como una cadena.
'''
print ("Programa solicitar puntuación entre 0.0 y 1.0")
print ("---------------------------------------------")

def computegrade():
    pun = float(input("Por favor, introduce puntuación entre 0.0 y 1.0: "))

    if  pun < 0.0 or pun > 1.0 :
        return "0"
    
    elif pun >= 0.9:
        return "A"

    elif pun >= 0.8:
        return "B"

    elif pun >= 0.7:
        return "C"

    elif pun >= 0.6:
        return "D"

    else:
        return "F"

    
valor = computegrade()
a=5
b=78

if valor=="0":
    print ("Error, por favor ha de introducir un número entre 0.0 y 1.0")

else: 
    print ("Su calificaión es: " + valor)
