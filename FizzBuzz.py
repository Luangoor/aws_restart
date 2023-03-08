lista = []
for i in range(1,51):
    if i % 5 == 0 and i % 3 == 0:
        lista.append("FizzBuzz")
    elif i % 3 == 0:
        lista.append("Fizz")
    elif i % 5 == 0:
        lista.append("Buzz")
    else:
        lista.append(str(i))
print(lista)