'''
Descarga una copia del archivo desde
http://www.py4e.com/code3/romeo.txt
Escribe un programa para abrir el archivo romeo.txt y léelo línea por línea. Para cada línea,
divide la línea en una lista de palabras usando la función split. Para cada palabra, 
verifica si la palabra ya está en una lista. Si la palabra no está en la lista, agrégala a la lista. 
Cuando se complete el programa, ordena e imprime las palabras resultantes en orden alfabético.
'''

def main():
    # Solicitar el nombre del archivo
    nombre_archivo = input("Introduce el nombre del archivo: ")
    try: 
        archivo = open(nombre_archivo)
    except:
        print("No se puede abrir el archivo:", nombre_archivo)

    # Inicializa una lista vacía para almacenar las palabras
    palabras = []
    
    # Lee cada línea del archivo
    for linea in archivo:
        # Divide la línea en una lista de palabras
        lista_palabras = linea.split()
        
        #Verifica cada palabra en la lista
        for palabra in lista_palabras:
            # Si la palabra no está en la lista, agrégala
            if palabra not in palabras:
                palabras.append(palabra)

    # Ordena la lista de palabras en orden alfabético
    palabras.sort()
    
    # Imprime las palabras ordenadas
    print (palabras)


main()


