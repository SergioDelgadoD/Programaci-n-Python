'''
EJERCICIO 11: Escribe otro programa que solicite una lista de números como arriba y 
al final imprima el máximo y el mínimo de los números en lugar del promedio.
''' 
count = 0
total = 0
lista = []

while (str(next := input("introduce número : "))!='listo'):
    try:
        total+=float(next)
        count+=1   
        lista.append(next)        
        
    except:
        print(f"Invalid number {next}\n")

if count == 0:
    print ("No se ha indicado ningun número")
else:
    print("Total: "+ str(total) +"\nCount: "+str(count)+"\nMayor: "+str(max(lista))+"\nMínimo: "+str(min(lista)))