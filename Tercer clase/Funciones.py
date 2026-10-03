def funcion1():
    print("Hola mundo")

def suma(a, b):
    return a + b

def añadir_usuario(nombre, edad, ciudad):
    print(f"usuario añadido: {nombre}, {edad} años, de {ciudad}")
    usuarios = {nombre: {"edad": edad, "ciudad": ciudad}}
    return usuarios


while True:
    print("Añadir usuarios")
    nombre = input("Ingrese el nombre del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    ciudad = input("Ingrese la ciudad del usuario: ")
    usuarios = añadir_usuario(nombre, edad, ciudad)