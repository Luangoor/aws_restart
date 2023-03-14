# coding=utf-8
"""
Reto Python v2. Encontrar los números primos desde 1 a un número
indicado por el usuario para guardarlos en el archivo results.txt
"""
# Pedimos el límite superior para la búsqueda.
print("Ingrese un número entero mayor a 2.")
limite = input("Buscar números primos de 1 a: ")

# Intentamos convertir la entrada del usuario a entero.
# Y verificamos que sea un número mayor a 2. 
try:
    limite = int(limite)
    assert limite > 2
except:
    print("Uso incorrecto. Intente de nuevo.")
    print("Debe ingresar un número entero mayor a 2.")
    exit(1)

primos = ""
contador = 0
# Ciclo for que recorre todos los números a partir de 2
# hasta el límite indicado. El 1 no se incluye porque no es
# un número primo.
for i in range(2,limite + 1):
    # Ciclo for anidado que recorre los números desde 2
    # hasta la raiz cuadrada de i redondeada hacia arriba.
    # Ya que si i tiene un divisor más grande que su raíz
    # entonces debe tener un divisor menor que su raíz.
    # Antes: for j in range(2, i+1):
    for j in range(2, int(i**0.5) + 2):
        # Comprueba si el número i tiene un divisor mayor
        # que 1 y distinto a i.
        # Si lo tiene interrumpe el ciclo.
        if i % j == 0 and i != j:
            break
        # Si no lo tiene y llegó al final del ciclo, añade
        # el número al string.
        # Antes: elif j == i:
        elif j == int(i**0.5) + 1:
            primos += str(i) + ", "
            contador += 1
# Borra la coma y el espacio del final
primos = primos[0:-2]
print("Los números primos son:")
print(primos)

# Intenta escribir el string de números primos en results.txt
try:
    with open("results.txt", "w") as file:
        file.write(primos)
except IOError:
    print("Error con el archivo. No se pudo abrir.")
    exit(2)
except:
    print("Error.")
    exit(3)
print(f"Hay {contador} números primos menores que {limite}")