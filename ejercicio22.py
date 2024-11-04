'''
Este programa registra el nombre de dominio (en lugar de la dirección) desde donde se envió 
el mensaje en lugar de a quién le llegó el correo (es decir, la dirección de correo electrónico completa). 
Al final del programa, imprime el contenido de tu diccionario.

python schoolcount.py Enter a file name: mbox-short.txt {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
<<<<<<< HEAD
'''
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
            correos = linea.split("@")[1]
        
        
            # Incrementar el contador en el diccionario
            if correos not in conteo_correos:
                conteo_correos[correos] = 1
            else:
                conteo_correos[correos] += 1
    
    # Cerrar el archivo
    archivo.close()

    # Imprimir el contenido del diccionario
    for correos, num in conteo_correos.items():
        print(correos, num)  

    # Imprimir todo el diccionario
    print (conteo_correos)

if __name__ == "__main__":
    main()
=======
'''
>>>>>>> 0fe10e78ab53b1fd79879686fad9e20dccf87a10
