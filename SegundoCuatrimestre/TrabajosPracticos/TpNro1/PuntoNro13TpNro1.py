# Se desea realizar una aplicación que solicite al usuario un caracter y un número
# natural N, y que la aplicación muestre en pantalla dicho carácter repetido N veces
# consecutivas.
# Ej: Ingrese un caracter: +
# Ingrese la cantidad de repeticiones: 15
# +++++++++++++++


Valor=input("Dame un caractero o numero natural ")
Cantidad=int(input("¿Cuantas veces lo repetimos? "))

for i in range(Cantidad):
    print(f"{Valor},", end=" ")    