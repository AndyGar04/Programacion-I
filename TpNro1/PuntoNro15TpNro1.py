# 15. Escriba un programa que, dada una oración ingresada muestre por pantalla:
# En este ejercicio, para simplificar, asumiremos que los posibles caracteres de
# entrada son letras, espacios, dígitos, signos de puntuación, signos de
# interrogación y de exclamación.
# Investigar si hay funciones de strings que nos faciliten la resolución [len(),
# .isalpha(), .split() , etc.]

Frase = input("Dame una frase ")
cont_letras = 0

# a. El número total de caracteres en la oración
print(f"El número total de caracteres es {len(Frase)}")

# b. La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
for i in range(len(Frase)):
    if Frase[i].isalpha():
        cont_letras += 1
print(f"Contando consonantes y vocales hay {cont_letras} letras")

# c. La cantidad de palabras separadas por uno o más espacios
cant_palabras = Frase.split()
print(f"Hay {len(cant_palabras)} palabras")



