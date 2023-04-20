# Fibonacci
# Inicializar lista con los primeros 2 valores.
fibonacci = [0, 1]
# Pedimos la cantidad de números deseada.
cantidad = int(input("Números de Fibonacci (mayor a 2): "))
# Creamos el siguiente valor y lo añadimos a la lista.
for i in range(2, (cantidad)):
    nuevoValor = fibonacci[i - 2] + fibonacci[i - 1]
    fibonacci.append(nuevoValor)
print(fibonacci)