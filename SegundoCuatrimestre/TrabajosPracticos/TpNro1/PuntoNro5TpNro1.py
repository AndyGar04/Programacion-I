#5. Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene.

CadenaDeTexto=input("Dame una frase")
Espacio=' '
Count=0

for i in CadenaDeTexto:
    if i == Espacio:
        Count += 1

print(f"La cantidad de espacios es {Count}")