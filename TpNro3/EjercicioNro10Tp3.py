# 10. Dada una lista de diccionarios que contienen información de estudiantes de una
# materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final) ,
# utilizando list comprehensions:
# a. Crea una lista que contenga los nombres de todos los estudiantes. Salida
# ejemplo: nombres: ['Pepe', 'María', 'Pedro', 'Ana']
# b. Crea una lista que contenga los nombres de todos los estudiantes que han
# obtenido una calificación superior a 70 en todos los exámenes
# c. Crea una lista que contenga los nombres de todos los estudiantes que han
# obtenido una calificación inferior a 60 en al menos un examen.

d = [
    {"nombre_apellido": "Juan Perez", "legajo": 12345, "nota_parcial1": 8, "nota_parcial2": 7, "nota_final": 9},
    {"nombre_apellido": "Maria Lopez", "legajo": 23456, "nota_parcial1": 6, "nota_parcial2": 7, "nota_final": 8},
    {"nombre_apellido": "Carlos Garcia", "legajo": 34567, "nota_parcial1": 9, "nota_parcial2": 8, "nota_final": 9},
    {"nombre_apellido": "Lucia Gomez", "legajo": 45678, "nota_parcial1": 5, "nota_parcial2": 6, "nota_final": 7},
    {"nombre_apellido": "Ana Martinez", "legajo": 56789, "nota_parcial1": 7, "nota_parcial2": 7, "nota_final": 8}
]

ListaNombres=list(nombres["nombre_apellido"] for nombres in d)
print(ListaNombres)
ListaNombresMasSiete=list(nombres["nombre_apellido"] for nombres in d if(nombres["nota_parcial1"]>=7 and nombres["nota_parcial2"]>=7))
print(ListaNombresMasSiete)
ListaNombresMenosSesenta=list(nombres["nombre_apellido"] for nombres in d if(nombres["nota_parcial1"]<=6 or nombres["nota_parcial2"]<=6))
print(ListaNombresMenosSesenta)