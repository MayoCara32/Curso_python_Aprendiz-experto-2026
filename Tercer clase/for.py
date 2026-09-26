# for_basico.py

gastos = [
    {"categoria": "Transporte", "monto": 35.0},
    {"categoria": "Alimentos", "monto": 82.5},
    {"categoria": "Materiales", "monto": 120.0},
]

total = 0

for gasto in gastos:
    print(f"{gasto['categoria']}: ${gasto['monto']:.2f}")
    total += gasto["monto"]

print(f"Total gastado: ${total:.2f}")

for clave, valor in gastos[0].items():
    print(f"{clave}: {valor}")