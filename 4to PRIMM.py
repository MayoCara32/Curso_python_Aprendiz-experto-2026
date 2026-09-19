#! condicionales
disponible = -12
if disponible > 0:
    print("aun tienes presupuesto")
elif disponible == 0:
    print("ya no tienes presupuesto, te lo gastaste todo")
else:
    print("ya no tienes presupuesto, te debes dinero")
    
#! Condicionales anidadas
gasto = float(input("Ingresa el gasto que realizaste: "))
if gasto < 0:
    print("El gasto no puede ser negativo")
elif gasto > 0:
    if gasto < 50:
        print("gastaste poco")
    elif gasto >= 50 and gasto < 100:
        print("gastaste un poco mas")
    else:
        print("gastaste mucho")

#! condicionales con caracteres
letra = input("Ingresa una letra: ").strip().lower()
if letra == "hola":
    print("Hola, soy un saludo")
else: 
    print("No soy un saludo")
