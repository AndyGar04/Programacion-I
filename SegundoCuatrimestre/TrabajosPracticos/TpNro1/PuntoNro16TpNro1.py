# 16. Escriba un programa que para un texto ingresado nos muestre cual es la palabra
# más larga dentro de ese texto y cuántas letras tiene.

texto = input("Ingrese un texto: ")

# Divide el texto en una lista de palabras
palabras = texto.split()

# Encuentra la palabra más larga
palabra_mas_larga = max(palabras, key=len)

# Calcula la cantidad de letras de la palabra más larga
cantidad_letras = len(palabra_mas_larga)

# Imprime el resultado
print(f"La palabra más larga es '{palabra_mas_larga}' con {cantidad_letras} letras.")
