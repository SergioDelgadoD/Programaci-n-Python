'''Escribe un programa que lea un registro de correo, cree un histograma usando un diccionario 
para contar cuántos mensajes has recibido de cada dirección de correo electrónico y luego imprima el diccionario.
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
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

main()