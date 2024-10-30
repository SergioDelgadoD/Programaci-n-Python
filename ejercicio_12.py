'''
EJERCICIO 12: Toma el siguiente código de Python que almacena una cadena:
"str = 'X-DSPAM-Confidence: 0.8475"

Usa "find" y el corte de cadena para extraer la parte de la cadena después del caracter de dos puntos y luego use la función "float" para convertir la cadena extraída en un número de punto flotante.
'''
str = 'X-DSPAM-Confidence: 0.8475'
start_pos = str.find(':') + 1
number_str = str[start_pos:].strip()
confidence = float(number_str)
print(confidence)

#otra forma de hacerlo
longitud= len(str)
print (float(str [start_pos:longitud]))

