def saludar():
    print("Hola, soy un saludo desde una función")

saludar()
saludar()
saludar()

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(10, 20)}")

def calcular_iva(precio, tasa_iva):
    iva = precio * tasa_iva
    total = precio + iva
    return total

total_con_iva = calcular_iva(100, 0.16)
print(f"El total con IVA es: {total_con_iva}")

def verificar_disponible(presupuesto, gasto):
    if presupuesto >= gasto:
        return True
    else:
        return False
verificacion = verificar_disponible(100, 50)
if verificacion:
    print("Aun tienes presupuesto")
else:
    print("Ya no tienes presupuesto, te lo gastaste todo")
