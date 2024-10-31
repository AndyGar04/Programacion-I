# Realizar un programa que solicite al usuario un número entero positivo, y luego en
# pantalla muestre la secuencia de números desde el 1 hasta el número ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10

NroIngresado=int(input("Dame un valor entero positivo"))

if NroIngresado<=0:
    print("Entero positivo te dije")
else:
    for i in range(NroIngresado+1):
        print(f"Contando vamos por el {i}")

                