# archivos_csv.py

import csv
from pathlib import Path


ARCHIVO = Path("gastos.csv")
CAMPOS = ("id", "categoria", "monto")


def guardar_gastos(gastos):
    with ARCHIVO.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=CAMPOS
        )

        escritor.writeheader()
        escritor.writerows(gastos)


def agregar_gasto(gasto):
    archivo_tiene_datos = (
        ARCHIVO.exists()
        and ARCHIVO.stat().st_size > 0
    )

    with ARCHIVO.open(
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=CAMPOS
        )

        if not archivo_tiene_datos:
            escritor.writeheader()

        escritor.writerow(gasto)


def cargar_gastos():
    if not ARCHIVO.exists():
        return []

    gastos = []

    with ARCHIVO.open(
        "r",
        newline="",
        encoding="utf-8"
    ) as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            gasto = {
                "id": int(fila["id"]),
                "categoria": fila["categoria"],
                "monto": float(fila["monto"]),
            }

            gastos.append(gasto)

    return gastos


gastos_iniciales = [
    {
        "id": 1,
        "categoria": "Transporte",
        "monto": 35.0,
    },
    {
        "id": 2,
        "categoria": "Alimentos",
        "monto": 82.5,
    },
]

guardar_gastos(gastos_iniciales)

agregar_gasto({
    "id": 3,
    "categoria": "Materiales",
    "monto": 120.0,
})

gastos_cargados = cargar_gastos()

for gasto in gastos_cargados:
    print(
        f"{gasto['id']}. "
        f"{gasto['categoria']}: "
        f"${gasto['monto']:.2f}"
    )