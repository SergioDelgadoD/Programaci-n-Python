'''
EJERCICIO 3: Supongamos que ejecutamos las siguientes instrucciones de asignación:
width = 17
height = 12.0

Para cada una de las siguientes expresiones, escriba el valor de la expresión y el tipo (del valor de la expresión). Use el intérprete de Python para verificar sus respuestas.
width//2
width/ 2.0
height/ 3
1+2*5
'''
width = 17
height = 12.0

print ("El resto de dividir " + str(width) + " entre 2 es: " + str(width//2),type(width//2))
print ("El resultado de dividir " +str(width) + " entre 2 es: " + str(width/ 2.0), type(width/ 2.0))
print ("El resultado de dividir " +str(height) + " entre 3 es: " + str(height/ 3), type(height/ 3))
print ("El resultado de (1+2*5) es: " + str(1+2*5), type (1+2*5))
