#! Calcular la disponibilidad de un presupuesto
def calcular_disponible(presupuesto, gasto):
    return presupuesto - gasto

def obtener_estado(disponible):
    if disponible > 0:
        return "Aun tienes presupuesto"
    elif disponible == 0:
        return "Ya no tienes dinero, lo gastaste todo"
    else:
        return "Ya no tienes dinero, debes dinero"
def main():
    print("Control de presupuesto")
    nombre = input("Ingrese su nombre: ")
    categoria = input("Ingrese la categoría de gasto: ")
    prespuesto = float(input("Ingrese su presupuesto: "))
    gasto = float(input("ingrese el gasto: "))
    valores_validos = prespuesto >= 0 and gasto >= 0    
    if not valores_validos:
        print("Los valores ingresados no son válidos. Por favor, ingrese números positivos.")
        return
    disponible = calcular_disponible(prespuesto, gasto)
    estado = obtener_estado(disponible)
    print("Resumen del presupuesto")
    print(f"Nombre: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Presupuesto: {prespuesto}")
    print(f"Gasto: {gasto}")
    print(f"Disponible: {disponible}")
    print(f"Estado: {estado}")
    print("Gracias por usar el sistema de control de presupuesto.")
main()
