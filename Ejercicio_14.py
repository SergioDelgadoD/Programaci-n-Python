'''
EJERCICIO 14: Escribe un programa para solicitar un nombre de archivo. Luego lee el archivo y busca las líneas del formulario:
X-DSPAM-Confidence: 0.8475

Cuando encuentra una línea que comienza con "X-DSPAM-Confidence:", separa la línea para extraer el número de punto flotante en la línea. Cuenta estas líneas y luego calcula el total de los valores de confianza de correo no deseado de estas líneas. Cuando llegues al final del archivo, imprime la confianza promedio del spam.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
'''
# Solicitar el nombre del archivo
nombre_archivo = input("Enter the file name: ")

# Intentar abrir el archivo
try:
    archivo = open(nombre_archivo)
except:
    print("No se puede abrir el archivo:", nombre_archivo)
    quit()

conteo_lineas = 0
total_confianza = 0.0

# Leer el archivo línea por línea
for linea in archivo:
    if linea.startswith("X-DSPAM-Confidence:"):
        # Separar la línea para obtener el valor de confianza
        partes = linea.split(":")
        confianza = float(partes[1].strip())
        total_confianza += confianza
        conteo_lineas += 1

# Calcular el promedio de confianza de spam
if conteo_lineas > 0:
    promedio_confianza = total_confianza / conteo_lineas
    print("Average spam confidence:", promedio_confianza)
else:
    print("No se encontraron líneas de confianza de spam en el archivo.")