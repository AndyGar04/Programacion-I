# 10. Se desea realizar una aplicación que solicite al usuario tres números enteros
# positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén
# entre A y B inclusive. 

a=int(input("Dame A (nro inicio)"))
b=int(input("Dame B (nro final)"))
x=int(input("Dame X"))

for i in range(a, b+1):
    if (x % i == 0):
        print(f"{i} es multiplo de X")