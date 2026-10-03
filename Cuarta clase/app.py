import csv
import io
import math


def validar_cantidad(valor, permite_cero=False):
    if isinstance(valor, bool):
        raise ValueError("La cantidad debe ser numérica.")

    try:
        cantidad = float(valor)
    except (TypeError, ValueError) as error:
        raise ValueError("Escribe una cantidad válida.") from error

    if not math.isfinite(cantidad):
        raise ValueError("La cantidad debe ser finita.")

    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    cantidad = round(cantidad, 2)

    if not permite_cero and cantidad == 0:
        raise ValueError("El gasto debe ser al menos de $0.01.")

    return cantidad


def crear_gasto(categoria, monto):
    if not isinstance(categoria, str):
        raise ValueError("La categoría debe ser texto.")

    categoria_limpia = categoria.strip()

    if not categoria_limpia:
        raise ValueError("La categoría no puede estar vacía.")

    return {
        "categoria": categoria_limpia.title(),
        "monto": validar_cantidad(monto),
    }


def calcular_total(gastos):
    return round(sum(gasto["monto"] for gasto in gastos), 2)


def calcular_disponible(presupuesto, gastos):
    presupuesto_valido = validar_cantidad(
        presupuesto,
        permite_cero=True,
    )

    return round(presupuesto_valido - calcular_total(gastos), 2)


def generar_csv(gastos):
    salida = io.StringIO(newline="")

    escritor = csv.DictWriter(
        salida,
        fieldnames=("categoria", "monto"),
    )

    escritor.writeheader()

    for gasto in gastos:
        escritor.writerow({
            "categoria": gasto["categoria"],
            "monto": f"{gasto['monto']:.2f}",
        })

    return salida.getvalue()