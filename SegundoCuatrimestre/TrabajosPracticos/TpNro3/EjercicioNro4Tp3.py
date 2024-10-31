# 4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo
# las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por
# el usuario, utilizando list comprehensions

diccionario = {
    "arbol": "Planta perenne de tallo leñoso.",
    "avión": "Aeronave más pesada que el aire, impulsada por motores.",
    "agua": "Sustancia líquida sin olor ni sabor, esencial para la vida.",
    "computadora": "Máquina electrónica que procesa datos.",
    "carro": "Vehículo de cuatro ruedas movido por un motor.",
    "bicicleta": "Vehículo de dos ruedas impulsado por pedales.",
    "almohada": "Objeto que se usa para apoyar la cabeza al dormir.",
    "espejo": "Superficie que refleja la luz y permite ver imágenes.",
    "elefante": "Mamífero de gran tamaño con una trompa larga.",
    "mesa": "Mueble con tablero sostenido por patas."
}

Char=input("Dame una letra ")

PalabrasQueCumplen=[palabra for palabra in diccionario if(palabra[0].lower()==Char.lower())]

print(PalabrasQueCumplen)

