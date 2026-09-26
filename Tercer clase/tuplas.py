# Crear tuplas
categorias_permitidas = (
    "Transporte",
    "Alimentos",
    "Materiales",
    "Servicios"
)

# Una tupla con un solo elemento necesita coma
categoria_unica = ("Salud",)

print(categorias_permitidas)
print(categoria_unica)

# Acceso por índice
print(categorias_permitidas[0])

# Slicing
print(categorias_permitidas[1:3])

# count: cuenta cuántas veces aparece un valor
categorias_repetidas = (
    "Transporte",
    "Alimentos",
    "Transporte",
    "Materiales"
)

print(categorias_repetidas.count("Transporte"))

# index: obtiene la posición de un valor
posicion = categorias_permitidas.index("Materiales")
print(posicion)

# Concatenar tuplas: crea una nueva tupla
categorias_extra = ("Salud", "Ocio")
todas_las_categorias = categorias_permitidas + categorias_extra
print(todas_las_categorias)

# Repetir valores
mensaje = ("Gasto registrado",) * 2
print(mensaje)

# Desempaquetado
primera, segunda, tercera, cuarta = categorias_permitidas
print(primera)
print(cuarta)

# in y len
if "Alimentos" in categorias_permitidas:
    print("Alimentos es una categoría permitida.")

print(len(categorias_permitidas))