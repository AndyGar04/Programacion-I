# 12. Escriba un programa que permita el ingreso de números enteros positivos,
# finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de
# menor a mayor.

Funcionamiento=True
Ordenado=False
Suma=0
Count=0
Lista=list()

while Funcionamiento:
    Nro=int(input("Dame un numero entero positivo"))
    if Nro<0:
        print("Error, no es un entero posivo")
        Funcionamiento=False
    else:    
     if Nro==0:
        for i in range(0, len(Lista)):
            if Lista[i] < Lista[i-1]:
                Ordenado=True
     if Ordenado==True:
      print("La lista esta ordenada de menor a mayor")        
      Funcionamiento=False
     else:
         Lista.insert(Count, Nro)
         Count+=1

print(Lista)