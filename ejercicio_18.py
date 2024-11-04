'''
Escribe un programa que solicita al usuario una lista de números e imprime el máximo y el mínimo 
de los números al final cuando el usuario ingresa "listo". Escribe el programa para almacenar los números 
que el usuario ingresa en una lista y use las funciones "max()" y "min()" para calcular los números máximo y mínimo 
después de que se complete el ciclo.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
'''
lista = []

while (str(next := input("introduce número: "))!='listo'):
    try:
        lista.append(float(next))
    except:
        print(f"Invalid number: {next}\n")

print("Mínimo: "+str(min(lista)))
print("Máximo: "+str(max(lista)))