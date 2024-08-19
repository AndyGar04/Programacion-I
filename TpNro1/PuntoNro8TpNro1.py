# 9. Desarrollar un programa que permita al usuario indicar cuantos valores quiere
# ingresar, luego que permita la carga de los valores por teclado y nos muestre
# posteriormente la suma de los valores ingresados y su promedio.

Cantidad=int(input("Dame la cantidad de valores que vas a ingresar "))
Suma=0

for i in range(Cantidad):
    Valor=int(input("Dame un numero "))
    Suma=Suma+Valor

promedio=Suma/Cantidad

print(f"El promedio de los valores ingresados es {promedio}")