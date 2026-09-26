# funciones_reutilizables.py

def crear_gasto(identificador, categoria, monto):
    return {
        "id": identificador,
        "categoria": categoria.strip().title(),
        "monto": float(monto),
    }


def calcular_total(gastos):
    return sum(gasto["monto"] for gasto in gastos)


def calcular_disponible(presupuesto, gastos):
    return float(presupuesto) - calcular_total(gastos)


def clasificar_saldo(disponible):
    if disponible > 0:
        return "Saldo positivo."
    if disponible == 0:
        return "Saldo cero."

    return "Saldo negativo."


def buscar_por_categoria(gastos, categoria):
    categoria_limpia = categoria.strip().title()

    return [
        gasto
        for gasto in gastos
        if gasto["categoria"] == categoria_limpia
    ]


def buscar_por_id(gastos, identificador):
    for gasto in gastos:
        if gasto["id"] == identificador:
            return gasto

    return None


def actualizar_monto(gastos, identificador, nuevo_monto):
    gasto = buscar_por_id(gastos, identificador)

    if gasto is None:
        raise KeyError("No existe ese identificador.")

    gasto["monto"] = float(nuevo_monto)
    return gasto


def eliminar_gasto(gastos, identificador):
    for indice, gasto in enumerate(gastos):
        if gasto["id"] == identificador:
            return gastos.pop(indice)

    raise KeyError("No existe ese identificador.")