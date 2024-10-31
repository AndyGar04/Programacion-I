# 2. Implemente una función que, dada una lista de nombres, devuelva una nueva lista
# que contenga solo los nombres que tengan una longitud mayor o igual a una
# cantidad de caracteres pasada por parámetro, utilizando list comprehensions

Nombres=["Marcos", "Pepe", "Fausto", "Federico", "Julian", "Sebastian", "Enrique"]
Caracteres=int(input("Dame una cantidad de caracteres"))

Nombres_Parametrados=[nombre for nombre in Nombres if(len(nombre)>=Caracteres)]

print(Nombres_Parametrados)

