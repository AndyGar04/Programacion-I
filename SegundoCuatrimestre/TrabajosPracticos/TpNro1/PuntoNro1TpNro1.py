#1. Realizar un programa que pida los tres lados de un triángulo e indique el tipo de
#triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos
#lados iguales) o Escaleno (tres lados distintos).

Lado1=int(input("Dame el lado 1: "))
Lado2=int(input("Dame el lado 2: "))
Lado3=int(input("Dame el lado 3: "))

if Lado1==Lado2 and Lado2==Lado3:
    print("El triangulo es equilatero")
elif Lado1==Lado2 or Lado2==Lado3:
    print("El triangulo es isoseles")
else:
    print("El triangulo es escaleno")        

