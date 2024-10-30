'''
EJERCICIO 4: Escribe un programa que solicite al usuario una temperatura en grados Celsius, 
convierta la temperatura a Fahrenheit e imprima la temperatura convertida
'''
celsius = int(input("Por favor, introduce una temperatura en grados Celsius: "))
Fahrenheit = (celsius * 9 / 5) + 32

print (str(celsius) + "Cº son "+ str(Fahrenheit) + "ºF")
