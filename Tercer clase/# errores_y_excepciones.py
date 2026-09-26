# errores_y_excepciones.py

class MontoInvalidoError(ValueError):
    pass


def dividir_presupuesto(presupuesto, cantidad_personas):
    try:
        resultado = presupuesto / cantidad_personas

    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
        return None

    except TypeError:
        print("Los datos deben ser números.")
        return None

    else:
        print(f"Resultado correcto: ${resultado:.2f}")
        return resultado

    finally:
        print("Operación de división terminada.")


def convertir_monto(texto):
    try:
        monto = float(texto)

    except ValueError as error:
        raise MontoInvalidoError(
            "El monto debe ser numérico."
        ) from error

    if monto <= 0:
        raise MontoInvalidoError(
            "El monto debe ser mayor que cero."
        )

    return monto


def leer_archivo(nombre_archivo):
    try:
        with open(
            nombre_archivo,
            "r",
            encoding="utf-8"
        ) as archivo:
            contenido = archivo.read()

    except FileNotFoundError:
        print("El archivo no existe.")
        return ""

    except PermissionError:
        print("No tienes permiso para leer el archivo.")
        return ""

    else:
        print("Archivo leído correctamente.")
        return contenido

    finally:
        print("Lectura de archivo finalizada.")


dividir_presupuesto(500, 5)
dividir_presupuesto(500, 0)

try:
    monto = convertir_monto("abc")
except MontoInvalidoError as error:
    print(f"Error controlado: {error}")

leer_archivo("archivo_inexistente.txt")