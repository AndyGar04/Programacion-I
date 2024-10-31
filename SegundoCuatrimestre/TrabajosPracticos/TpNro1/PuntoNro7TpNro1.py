#Realizar un programa que solicite al usuario un número entero positivo, y luego en
#pantalla muestre solamente los números pares desde el 1 hasta el número
#ingresado.
#Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10

NroIngresado=int(input("Dame un valor entero positivo"))

if NroIngresado<=0:
    print("Entero positivo te dije")
else:
    for i in range(NroIngresado+1):
        if (i % 2 == 0):
         print(f"Contando vamos por el {i}")