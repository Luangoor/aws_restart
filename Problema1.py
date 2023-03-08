"""
Problema 1
Se necesita un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por
una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido para
mostrar el consumo de combustible por kilómetro.
Input: Kilómetros recorridos (float > 0), Litros de combustible gastados (float > 0)
Output: Consumo por kilómetro.
Ejemplo de ejecución:
Kilómetros recorridos: 260
Litros de combustible gastados: 12.5
El consumo por kilómetro es de 20.8
"""
print("Calculadora de consumo por km")
km = float(input("Kilometros recorridos: "))
combustible = float(input("Litros de combustible gastados: "))
print(f"El consumo de km/l es de: {km/combustible}")