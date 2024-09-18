'''
# lista = Rodrigo , Lucas , Luciano , Daniel

nombres = ['Rodri', 'Juli', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) # Solo muestra el indica 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[2] = 'Cacho'
nombres[3] = 'Maria'
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice específico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Walter')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento
nombres.pop() # Si no indicamos el indice, elimina el ultimo indice
print(nombres)

del nombres[2] # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres)
'''

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
