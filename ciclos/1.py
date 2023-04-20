# Lo hice en una lista para ver mejor los resultados
lista = []
for i in range(1,51):
    if i % 5 == 0:
        if i % 3 == 0:
            lista.append("FizzBuzz")
        else:
            lista.append("Buzz")
    elif i % 3 == 0:
        lista.append("Fizz")
    else:
        lista.append(str(i))
# Utilizando un join para imprimirlo
print(" ".join(lista))