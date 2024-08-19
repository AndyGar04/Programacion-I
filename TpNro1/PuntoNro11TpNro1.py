# 11. Escriba un programa que permita el ingreso de números enteros positivos para
# calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número
# negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej:
# “El promedio es ….. con un total de …. ingresos.”

Funcionamiento=True
Suma=0
Count=0

while Funcionamiento:
    Nro=int(input("Dame un numero "))
    if Nro>=0:
        Suma=Suma+Nro
        Count+=1
    else:
        print(f"El promedio es {(Suma/Count)} con un total de {Count} ingresos")
        Funcionamiento=False


