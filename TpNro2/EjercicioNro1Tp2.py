# 1. Escribir un procedimiento “reverso” que permita ingresar como parámetro una
# cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). 
# 
# Escribir luego un programa que determine si una cadena de caracteres es un palíndromo (un
# palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”).

# Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas,
# utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es
# distinto a radaR.

def Invertir_palabra(palabra):
    global palabra_invertida
    palabra_invertida = ""
    caracteres=len(palabra)-1
    for i in range(len(palabra)):
        palabra_invertida += palabra[caracteres]
        caracteres-=1                

def Palindromo_palabra(palabra):
    global palindromo
    palindromo = True
    
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[len(palabra) - i - 1]:
            palindromo = False

Palabreichon = input("Dame una palabra ")
Palabreichon = Palabreichon.lower()
Palindromo_palabra(Palabreichon)
Invertir_palabra(Palabreichon)

print(f"Palabra invertida = {palabra_invertida}")

if (palindromo):
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")
