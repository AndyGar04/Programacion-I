# 7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de
# vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste
# introduzca la palabra “salir”.

Bandera=True
vocales="aeiou"

while Bandera:
    Palabra=input("Dame una palabra o escriba salir ")
    palabra=Palabra.lower()
    CantidadVocales=sum(1 for letra in palabra if letra.lower() in vocales)
    print(f"Tiene {CantidadVocales} vocales")
    if(palabra=="salir"):
        print("Saliste!")
        Bandera=False
    else:
        print("Que bueno, te quedaste!")    