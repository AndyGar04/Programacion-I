# 4. Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el
# mayor de los 3 y mostrar un mensaje por pantalla.

Nro1=int(input("Dame un numero" ))
Nro2=int(input("Dame un numero" ))
Nro3=int(input("Dame un numero" ))

if Nro1>Nro2 and Nro1>Nro3:
    print(f"El nro {Nro1} es el mas grande")
elif Nro2>Nro3:
    print(f"El nro {Nro2} es el mas grande")  
else:
    print(f"El nro {Nro3} es el mas grande")
