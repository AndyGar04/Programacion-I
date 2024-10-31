# 4. Escriba un programa que permita ingresar un número, se debe validar que
# realmente se haya ingresado un número, y crear una lista para almacenar por
# separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
# contiene el dígito mayor.

try:
    Num=int(input("Dame un numero"))
    Digitos=list()
    buleano=True
    aux=0
    pos=0

    while buleano:
        if (Num>10):
            Digitos.append(Num//10)
            Num=Num%10
        else:
            Digitos.append(Num)    
            buleano=False
    print(Digitos)
    for i in range(len(Digitos)):
        if (Digitos[i]>aux):
         pos=i
         aux=Digitos[i]
    print(f"El numero mas alto es {aux}")                 
except ValueError:
    print("Te pedi un numero...")
finally:
    print("Terminamo")        
