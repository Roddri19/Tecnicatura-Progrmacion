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

# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes, NO PARENTESIS

print(cocina[0])

# Mostrar la manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea de un elemento; la coma.
# De lo contrario solo sería un tipo string: cadena.

# Recorremos los elementos de la tupla
for cocinar in cocina: # Print está usando \n para saltos de líneas.
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de líneas.

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina, con esto eliminamos la tupla.

