# range_enumerate.py

categorias = [
    "Transporte",
    "Alimentos",
    "Materiales",
]

for numero in range(1, 6):
    print(f"Vuelta número {numero}")

for indice, categoria in enumerate(categorias, start=1):
    print(f"{indice}. {categoria}")

for numero in range(0, 21, 5):
    print(f"Cantidad: {numero}")