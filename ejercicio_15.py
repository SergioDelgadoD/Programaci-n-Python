'''
EJERCICIO 15: Escriba una función llamada "chop" que tome una lista y la modifique, eliminando el primer y último elemento 
y devuelva "None".
Luego escribe una función llamada "middle" que tome una lista y devuelva una nueva lista que contiene todos los elementos, 
excepto el primero y el último.
'''

def chop(lista):
    
    #Esta función toma una lista, elimina el primer y último elemento y devuelve None.
    if len(lista) > 1:
        del lista[0]
        del lista[-1]
    return None

def middle(lista):
    
    #Esta función toma una lista y devuelve una nueva lista con todos los elementos, excepto el primero y el último.
    return lista[1:-1] if len(lista) > 1 else []

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
print("Lista original:", mi_lista)

# Usando la función chop
chop(mi_lista)
print("Después de chop:", mi_lista)

# Usando la función middle
nueva_lista = middle([1,2,3])
print("Lista middle:", nueva_lista)
