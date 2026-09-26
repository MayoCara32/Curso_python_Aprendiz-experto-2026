# menu_while.py

while True:
    print("\n=== MENÚ ===")
    print("1. Registrar gasto")
    print("2. Mostrar gastos")
    print("3. Mostrar resumen")
    print("0. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        print("Registrar gasto.")
    elif opcion == "2":
        print("Mostrar gastos.")
    elif opcion == "3":
        print("Mostrar resumen.")
    elif opcion == "0":
        print("Programa terminado.")
        break
    else:
        print("Opción no válida.")