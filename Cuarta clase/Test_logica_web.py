import csv
import io

import pytest

from logica_web import (
    calcular_disponible,
    calcular_total,
    crear_gasto,
    generar_csv,
    validar_cantidad,
)


def test_crear_gasto_limpia_categoria():
    assert crear_gasto("  transporte  ", "35.50") == {
        "categoria": "Transporte",
        "monto": 35.5,
    }


@pytest.mark.parametrize(
    "categoria",
    ["", "   ", None],
)
def test_rechaza_categoria_invalida(categoria):
    with pytest.raises(ValueError):
        crear_gasto(categoria, 10)


@pytest.mark.parametrize(
    "monto",
    ["abc", -5, 0, "nan", "inf", True],
)
def test_rechaza_monto_invalido(monto):
    with pytest.raises(ValueError):
        crear_gasto("Materiales", monto)


def test_presupuesto_puede_ser_cero():
    assert validar_cantidad(0, permite_cero=True) == 0


def test_calculos_con_varios_gastos():
    gastos = [
        crear_gasto("Transporte", 35.5),
        crear_gasto("Alimentos", 82.5),
    ]

    assert calcular_total(gastos) == 118.0
    assert calcular_disponible(100, gastos) == -18.0


def test_lista_vacia():
    assert calcular_total([]) == 0
    assert calcular_disponible(500, []) == 500


def test_csv_conserva_categoria_con_coma():
    gastos = [
        crear_gasto("Materiales, laboratorio", 120),
    ]

    contenido = generar_csv(gastos)
    filas = list(csv.DictReader(io.StringIO(contenido)))

    assert filas == [{
        "categoria": "Materiales, Laboratorio",
        "monto": "120.00",
    }]