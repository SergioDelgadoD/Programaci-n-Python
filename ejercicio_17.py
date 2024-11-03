'''
Escribe un programa para leer los datos del buzón de correo y cuando encuentre la línea que comienza con "From", 
dividirá la línea en palabras usando la función split. Estamos interesados ​​en quién envió el mensaje, 
que es la segunda palabra en la línea From.
Analizará la línea Desde e imprimirá la segunda palabra para cada línea From, 
también contará el número de líneas From (no From:) e imprimirá un recuento al final. 
Esta es una buena salida de muestra con algunas líneas eliminadas:
python fromcount.py  
Enter a file name: mbox-short.txt  
stephen.marquard@uct.ac.za  
louis@media.berkeley.edu  
zqian@umich.edu  

[...some output removed...]  

ray@media.berkeley.edu  
cwen@iupui.edu  
cwen@iupui.edu  
cwen@iupui.edu  
There were 27 lines in the file with From as the first word  
'''
def main():
    # Solicitar el nombre del archivo
    nombre_archivo = input("Introduce el nombre del archivo: ")
    try: 
        archivo = open(nombre_archivo)
    except:
        print("No se puede abrir el archivo:", nombre_archivo)
    
    # Inicializar el contador de líneas "From"
    contador = 0

    # Leer cada línea del archivo
    for linea in archivo:
        # Eliminar espacios en blanco al inicio y al final de la línea
        linea = linea.strip()
        
        # Verificar si la línea empieza con "From: "
        if linea.startswith('From:'):
            # Dividir la línea en palabras
            palabras = linea.split()
            print (palabras)
            # Imprimir la segunda palabra (el remitente)
            print(palabras[1])
            
            # Incrementar el contador
            contador += 1

    # Imprimir el recuento total de líneas "From"
    print('Líneas From:', contador)

main()