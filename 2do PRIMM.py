#!Tipos de operaciones en python
numerica = 10 
flotante = 34.6
print("Debemos tener cuidado al operar con diferentes tipos de variables, ya que podemos tener errores de tipo")
print("Podemos subar una variable de tipo entero con una variable de tipo flotante, pero no podemos sumar una variable de tipo entero con una variable de tipo cadena de texto")
print(f"la suma de {numerica} + {flotante} es: {numerica + flotante}")
num1 = 23
print (f"La division del numero {num1} entre 2 es: {num1/2}")
respuesta = int(input("Ingrese un numero: "))
print(f"el numero ingresado es: {respuesta}")
print(f"la suma de {respuesta} + {num1} es: {respuesta + num1}")
num1 = input("Ingrese un numero: ")
num2 = input("Ingrese otro numero: ")
print(f"la suma de {num1} + {num2} es: {num1 + num2} y el tipo de dato es: {type(num1 + num2)}")
