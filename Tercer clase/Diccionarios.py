# Crear un diccionario
gasto = {
    "categoria": "Transporte",
    "monto": 35.0,
    "pagado": True
}

print(gasto)

# Acceder a un valor mediante su clave
print(gasto["categoria"])

# get: obtiene un valor sin provocar error si no existe
descripcion = gasto.get("descripcion", "Sin descripción")
print(descripcion)

# Agregar o modificar una clave
gasto["fecha"] = "2026-09-26"
gasto["monto"] = 40.0

# setdefault: agrega una clave sólo si no existe
gasto.setdefault("moneda", "MXN")
gasto.setdefault("moneda", "USD")  # No reemplaza el valor existente

# update: agrega o actualiza varios valores
gasto.update({
    "categoria": "Transporte urbano",
    "pagado": False
})

# keys: muestra las claves
print(gasto.keys())

# values: muestra los valores
print(gasto.values())

# items: muestra pares clave-valor
for clave, valor in gasto.items():
    print(f"{clave}: {valor}")

# in: comprueba si existe una clave
if "monto" in gasto:
    print("El gasto tiene monto.")

# pop: elimina una clave y devuelve su valor
moneda = gasto.pop("moneda")
print(f"Moneda eliminada: {moneda}")

# pop con valor por defecto
proveedor = gasto.pop("proveedor", "No registrado")
print(proveedor)

# copy: crea una copia
copia_gasto = gasto.copy()

# fromkeys: crea un diccionario con claves iniciales
categorias = ["Transporte", "Alimentos", "Materiales"]
presupuestos = dict.fromkeys(categorias, 0.0)
print(presupuestos)

# popitem: elimina y devuelve el último par agregado
ultimo_dato = copia_gasto.popitem()
print(f"Último dato eliminado: {ultimo_dato}")

# clear: elimina todo el contenido
copia_gasto.clear()
print(copia_gasto)