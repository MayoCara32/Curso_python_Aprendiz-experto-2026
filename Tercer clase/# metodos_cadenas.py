# metodos_cadenas.py

categoria = "  transporte urbano  "

limpia = categoria.strip()
print(limpia)

print(limpia.lower())
print(limpia.upper())
print(limpia.title())
print(limpia.capitalize())
print(limpia.replace("urbano", "público"))

print(limpia.startswith("trans"))
print(limpia.endswith("urbano"))
print("porte" in limpia)

texto = "transporte,alimentos,materiales"
lista_categorias = texto.split(",")
print(lista_categorias)

texto_nuevo = " | ".join(lista_categorias)
print(texto_nuevo)

print("Python".isalpha())
print("12345".isdigit())
print("A123".isalnum())
print("   ".isspace())

respuesta = input("¿Deseas continuar? (si/no): ").strip().lower()

if respuesta == "si":
    print("Continuamos.")
elif respuesta == "no":
    print("Programa terminado.")
else:
    print("Respuesta no válida.")