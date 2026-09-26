# test_funciones.py

import pytest

from funciones_reutilizables import (
    actualizar_monto,
    calcular_disponible,
    calcular_total,
    crear_gasto,
    eliminar_gasto,
    buscar_por_categoria,
)


def crear_gastos_prueba():
    return [
        crear_gasto(1, "Transporte", 35.0),
        crear_gasto(2, "Alimentos", 60.0),
        crear_gasto(3, "Materiales", 120.0),
    ]


def test_calcular_total():
    gastos = crear_gastos_prueba()

    assert calcular_total(gastos) == 215.0


def test_calcular_disponible():
    gastos = crear_gastos_prueba()

    assert calcular_disponible(500.0, gastos) == 285.0


def test_buscar_por_categoria():
    gastos = crear_gastos_prueba()

    resultado = buscar_por_categoria(
        gastos,
        "transporte"
    )

    assert len(resultado) == 1
    assert resultado[0]["monto"] == 35.0


def test_actualizar_monto():
    gastos = crear_gastos_prueba()

    gasto = actualizar_monto(gastos, 2, 90.0)

    assert gasto["monto"] == 90.0


def test_eliminar_gasto():
    gastos = crear_gastos_prueba()

    gasto_eliminado = eliminar_gasto(gastos, 1)

    assert gasto_eliminado["categoria"] == "Transporte"
    assert len(gastos) == 2


def test_eliminar_gasto_inexistente():
    gastos = crear_gastos_prueba()

    with pytest.raises(KeyError):
        eliminar_gasto(gastos, 99)