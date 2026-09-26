# sustituto_switch_diccionario.py

def registrar():
    print("Registrar gasto.")


def mostrar():
    print("Mostrar gastos.")


def resumen():
    print("Mostrar resumen.")


acciones = {
    "1": registrar,
    "2": mostrar,
    "3": resumen,
}

while True:
    print("\n=== MENÚ CON DICCIONARIO ===")
    print("1. Registrar gasto")
    print("2. Mostrar gastos")
    print("3. Mostrar resumen")
    print("0. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "0":
        print("Programa terminado.")
        break

    accion = acciones.get(opcion)

    if accion is None:
        print("Opción no válida.")
    else:
        accion()