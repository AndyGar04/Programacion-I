# 6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los
# nombres de las personas cuya edad es mayor a una edad ingresada por el usuario,
# utilizando list comprehensions.

ListaNombres=list()

d = {
    "Juan": 25,
    "María": 32,
    "Pedro": 19,
    "Ana": 45,
    "Luis": 22,
    "Carla": 28,
    "Jorge": 35
}

LimiteEdad=int(input("Dame una edad"))

ListaNombres=[nombre for nombre in d if(d[nombre]>LimiteEdad)]
print(list(ListaNombres))