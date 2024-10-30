'''
EJERCICIO 10: Escribe un programa que lea números repetidamente hasta que el usuario ingrese "listo". 
Una vez que se ingrese "listo", imprima el total, el recuento y el promedio de los números. Si el usuario 
ingresa algo que no sea un número, detecta su error usando "try" y "except" e imprime un mensaje de error 
y salta al siguiente número. Ejemplo de ejecución:
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''
count = 0
total = 0

while(str(next := input("introduce número : "))!='listo'):
    try:
        total+=float(next)
        count+=1
    except:
        print(f"Invalid number {next}\n")

if count == 0:
    print ("No se ha indicado ningun número")
else:
    print("Total: "+ str(total) +"\nCount: "+str(count)+"\nPromedio: "+str(total/count))