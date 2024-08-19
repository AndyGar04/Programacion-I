# 10. Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un
# rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje
# en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más
# largo, con el fin de evitar problemas de visualización en la consola. Verificar en los
# datos de entrada que se cumpla este requisito.

Lado1=int(input("Dame la medida de un lado "))
Lado2=int(input("Dame la medida del otro lado "))

if Lado1>40 or Lado2>40:
    print("Error, el limite posible es 40")
else:
    for i in range(Lado2):
     for j in range(Lado1):
         print ("* ", end=" ") 
     print(" ")