#! En Python tenemos diferentes estructuras de datos, como listas, tuplas y diccionarios. 
# A continuación se presentan algunos ejemplos de cómo se pueden utilizar estas estructuras para almacenar información sobre gastos.
#!Listas
# Crear listas
gastos = ["Transporte", "Alimentos", "Materiales"]
montos = [35.0, 82.5, 120.0, 12, 1234]

print(gastos)
print(montos)

# Acceso por índice
print(gastos[0])       # Transporte
print(gastos[-2])      # Materiales

# Slicing
print(gastos[0:5])     # Transporte y Alimentos

# append: agrega un elemento al final
gastos.append("Ocio")

# extend: agrega varios elementos
gastos.extend(["Salud", "Servicios"])

# insert: agrega un elemento en una posición específica
gastos.insert(1, "Cafetería")

# remove: elimina la primera coincidencia
gastos.remove("Ocio")

# pop: elimina y devuelve un elemento
ultimo_gasto = gastos.pop()
print(f"Gasto eliminado: {ultimo_gasto}")

# index: obtiene la posición de un valor
posicion = gastos.index("Alimentos")
print(f"Alimentos está en la posición {posicion}")

# count: cuenta repeticiones
gastos.append("Transporte")
print(gastos.count("Transporte"))

# copy: crea una copia independiente
copia_gastos = gastos.copy()

# reverse: invierte el orden de la lista
copia_gastos.reverse()
print(copia_gastos)

# sort: ordena la lista original
gastos.sort()
print(gastos)

# sort con reverse=True: orden descendente
montos.sort(reverse=True)
print(montos)

# in: comprueba si existe un valor
if "Transporte" in gastos:
    print("Hay gastos de transporte.")

# len: cantidad de elementos
print(f"Cantidad de categorías: {len(gastos)}")

# del: elimina por posición
del gastos[0]

# clear: elimina todos los elementos
copia_gastos.clear()
print(copia_gastos)

