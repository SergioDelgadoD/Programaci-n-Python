'''Agrega código al programa anterior para averiguar quién tiene más mensajes en el archivo. 
Una vez que hayas leído todos los datos y se haya creado el diccionario, examina el diccionario 
utilizando un bucle máximo para encontrar quién tiene más mensajes e imprime cuántos mensajes tiene la persona.

Enter a file name: mbox-short.txt cwen@iupui.edu 5

<<<<<<< HEAD
Enter a file name: mbox.txt zqian@umich.edu 195'''

def main():
    # Solicitar el nombre del archivo
    nombre_archivo = input("Introduce el nombre del archivo: ")
    try: 
        archivo = open(nombre_archivo)
    except:
        print("No se puede abrir el archivo:", nombre_archivo)
    
    # Inicializar un diccionario para contar los días de la semana
    conteo_correos = {}

    # Leer cada línea del archivo
    for linea in archivo:
        # Eliminar espacios en blanco al inicio y al final de la línea
        linea = linea.strip()
        
        # Verificar si la línea empieza con "From: "
        if linea.startswith('From: '):
            # Dividir la línea en palabras
            correos = linea.split()
        
            # Buscar la segunda palabra (correo)
            correo = correos[1]
        
            # Incrementar el contador en el diccionario
            if correo not in conteo_correos:
                conteo_correos[correo] = 1
            else:
                conteo_correos[correo] += 1
    
    # Cerrar el archivo
    archivo.close()

    # Imprimir el contenido del diccionario
    for correo in conteo_correos.items():
        print (correo) # conteo
    
    # Encontrar el correo con el máximo conteo
    max_correo = None
    max_conteo = 0
    
    for correo, conteo in conteo_correos.items():
        if conteo > max_conteo:
            max_conteo = conteo
            max_correo = correo

    # Imprimir quién tiene más mensajes
    if max_correo is not None:
        print("---------------------")
        print(f"El correo {max_correo} tiene el que más correos {max_conteo}")

if __name__ == "__main__":
    main()

