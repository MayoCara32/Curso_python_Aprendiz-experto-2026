# validaciones.py

from math import isfinite


CATEGORIAS_PERMITIDAS = (
    "Transporte",
    "Alimentos",
    "Materiales",
    "Servicios",
    "Salud",
    "Ocio",
)


def validar_categoria(categoria):
    categoria_limpia = categoria.strip().title()

    if categoria_limpia == "":
        raise ValueError("La categoría no puede estar vacía.")

    if categoria_limpia not in CATEGORIAS_PERMITIDAS:
        raise ValueError(
            "Categoría no permitida. "
            f"Opciones: {', '.join(CATEGORIAS_PERMITIDAS)}"
        )

    return categoria_limpia


def validar_monto(texto, permite_cero=False):
    monto = float(texto)

    if not isfinite(monto):
        raise ValueError(
            "El monto no puede ser infinito ni NaN."
        )

    if permite_cero and monto < 0:
        raise ValueError("El monto no puede ser negativo.")

    if not permite_cero and monto <= 0:
        raise ValueError(
            "El monto debe ser mayor que cero."
        )

    return monto


def pedir_categoria():
    while True:
        try:
            categoria = input("Categoría: ")
            return validar_categoria(categoria)
        except ValueError as error:
            print(f"Entrada inválida: {error}")


def pedir_monto(mensaje="Monto: $", permite_cero=False):
    while True:
        try:
            texto = input(mensaje)
            return validar_monto(texto, permite_cero)
        except ValueError as error:
            print(f"Entrada inválida: {error}")