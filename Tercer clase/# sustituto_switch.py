# sustituto_switch.py
# Requiere Python 3.10 o superior.

def registrar():
    print("Registrar gasto.")


def mostrar():
    print("Mostrar gastos.")


def resumen():
    print("Mostrar resumen.")
    

while True:
    print("\n=== MENÚ CON MATCH/CASE ===")
    print("1. Registrar gasto")
    print("2. Mostrar gastos")
    print("3. Mostrar resumen")
    print("0. Salir")

    opcion = input("Elige una opción: ").strip()

    match opcion:
        case "1":
            registrar()
        case "2":
            mostrar()
        case "3":
            resumen()
        case "0":
            print("Programa terminado.")
            break
        case _:
            print("Opción no válida.")