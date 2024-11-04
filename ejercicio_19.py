'''
Escribe un programa que categorice cada mensaje de correo según el día de la semana 
en que se realizó la confirmación. Para hacer esto, busca líneas que comiencen con "From", 
luego busca la tercera palabra y manten un conteo de cada uno de los días de la semana. 
Al final del programa, imprime el contenido de tu diccionario (el orden no importa).
Línea de muestra:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Ejecución de la muestra:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}  
'''
def main():
    # Solicitar el nombre del archivo
    nombre_archivo = input("Introduce el nombre del archivo: ")
    try: 
        archivo = open(nombre_archivo)
    except:
        print("No se puede abrir el archivo:", nombre_archivo)
    
    # Inicializar un diccionario para contar los días de la semana
    conteo_dias = {}

    # Leer cada línea del archivo
    for linea in archivo:
        # Eliminar espacios en blanco al inicio y al final de la línea
        linea = linea.strip()
        
        # Verificar si la línea empieza con "From "
        if linea.startswith('From '):
            # Dividir la línea en palabras
            palabras = linea.split()
        
            # Buscar la tercera palabra (el día de la semana)
            dia = palabras[2]
        
            # Incrementar el contador en el diccionario
            if dia not in conteo_dias:
                conteo_dias[dia] = 1
            else:
                conteo_dias[dia] += 1
    
    # Cerrar el archivo
    archivo.close()

    # Imprimir el contenido del diccionario
    for dia in conteo_dias.items():
        print (dia) # conteo

main()