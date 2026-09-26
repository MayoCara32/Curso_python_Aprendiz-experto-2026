# break_continue.py

montos = [35.0, 0.0, -5.0, 80.0, 250.0, 40.0]

for monto in montos:
    if monto <= 0:
        print(f"Se ignoró el monto ${monto:.2f}")
        continue

    print(f"Monto válido: ${monto:.2f}")

    if monto > 200:
        print("Se encontró un gasto mayor a $200.")
        break