# while_basico.py

respuesta = ""

while respuesta != "salir":
    respuesta = input(
        "Escribe una categoría o 'salir': "
    ).strip().lower()

    if respuesta == "salir":
        print("Programa terminado.")
    elif respuesta == "":
        print("No escribiste una categoría.")
    else:
        print(f"Categoría registrada: {respuesta.title()}")