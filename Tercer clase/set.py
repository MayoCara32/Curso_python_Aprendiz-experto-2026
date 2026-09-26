# Crear sets
categorias_usadas = {"Transporte", "Alimentos", "Transporte"}
print(categorias_usadas)

# Crear set desde una lista: elimina duplicados
categorias_lista = [
    "Transporte",
    "Alimentos",
    "Transporte",
    "Materiales"
]

categorias_unicas = set(categorias_lista)
print(categorias_unicas)

# add: agrega un elemento
categorias_usadas.add("Materiales")

# update: agrega varios elementos
categorias_usadas.update(["Salud","Ocio"])

# in: comprobar existencia
if "Transporte" in categorias_usadas:
    print("Se registraron gastos de transporte.")

# remove: elimina un elemento; genera error si no existe
categorias_usadas.remove("Ocio")

# discard: elimina sin generar error si no existe
categorias_usadas.discard("Viajes")

# copy: crea una copia
copia_categorias = categorias_usadas.copy()

# pop: elimina un elemento arbitrario
categoria_eliminada = copia_categorias.pop()
print(f"Elemento eliminado: {categoria_eliminada}")

# clear: elimina todos los elementos
copia_categorias.clear()
print(copia_categorias)

# Sets para comparar grupos
categorias_permitidas = {
    "Transporte",
    "Alimentos",
    "Materiales",
    "Servicios"
}

categorias_registradas = {
    "Transporte",
    "Alimentos",
    "Ocio"
}

# union: todos los elementos sin repetir
print(categorias_permitidas.union(categorias_registradas))

# intersection: elementos presentes en ambos sets
print(categorias_permitidas.intersection(categorias_registradas))

# difference: elementos del primer set que no están en el segundo
print(categorias_registradas.difference(categorias_permitidas))

# symmetric_difference: elementos que sólo están en uno de los sets
print(
    categorias_permitidas.symmetric_difference(categorias_registradas)
)

# issubset: comprobar si todos los elementos pertenecen a otro set
print(categorias_registradas.issubset(categorias_permitidas))

# issuperset: comprobar si contiene todos los elementos de otro set
print(categorias_permitidas.issuperset(categorias_registradas))

# isdisjoint: comprobar si no comparten elementos
print(categorias_registradas.isdisjoint({"Salud", "Servicios"}))

# Métodos que modifican el set original
copia = categorias_registradas.copy()
copia.intersection_update(categorias_permitidas)
print(copia)

copia = categorias_registradas.copy()
copia.difference_update(categorias_permitidas)
print(copia)

copia = categorias_registradas.copy()
copia.symmetric_difference_update(categorias_permitidas)
print(copia)