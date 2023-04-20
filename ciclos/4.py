# Inicializar lista
numeros = []
# Pedir números hasta que introduzcan 0
# Descartar los negativos
while True:
    num = int(input("Ingrese un número, 0 para continuar: "))
    if num == 0:
        break
    elif num < 0:
        continue
    else:
        numeros.append(num)
# Revisar si la lista no está vacia.
if len(numeros) > 0:
    print(f"Mayor número ingresado: {max(numeros)}")
else:
    print("No ingresó números positivos.")
    