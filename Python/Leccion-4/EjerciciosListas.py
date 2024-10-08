# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejercicio de ejecución: 0,3,6,9

print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de números de 2 a 6 e imprimirlos
# Ejemplo de ejecución: 2,3,4,5,6

print('Rango de numeros de 2 a 6 e imprimirlos')
for i in range(7):
    if i > 1 and i < 7:
        print(i)

# Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecución: 3,5,7,9

print('Crear un rango de 3 a 10 pero con incremento de 2 en 2')
for i in range(2,11,2):
    print(i)