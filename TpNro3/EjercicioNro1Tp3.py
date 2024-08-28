# 1. Implemente una función que, dada una lista de números, devuelva una nueva lista
# que contenga el cuadrado de cada número utilizando list comprehensions.

Numeros = [0,1,2,3,4,5,6,7,8,9]
print(Numeros)
Numeros = [numero**2 for numero in range(len(Numeros))]
print(Numeros)