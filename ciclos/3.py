# Ingresar 6 enteros
# Mostrar suma de negativos y promedio de positivos.
Numeros = []
Numeros.append(int(input("Número 1: ")))
Numeros.append(int(input("Número 2: ")))
Numeros.append(int(input("Número 3: ")))
Numeros.append(int(input("Número 4: ")))
Numeros.append(int(input("Número 5: ")))
Numeros.append(int(input("Número 6: ")))

# Armar una lista para números positivos y negativos.
Positivos, Negativos = [], []
for num in Numeros:
    if num > 0:
        Positivos.append(num)
    else:
        Negativos.append(num)

# Suma de números negativos
if len(Negativos) > 0:
    print(f"Suma de números negativos: {sum(Negativos)}")
else:
    print("No hay números negativos.")

# Promedio de positivos evitando división por 0.
if len(Positivos) > 0:
    print(f"Promedio de números positivos: {(sum(Positivos)) / len(Positivos)}")
else:
    print("No hay números positivos.")
