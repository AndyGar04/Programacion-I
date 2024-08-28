# 9. Dada una lista de números, crea dos listas separadas: una que contenga los
# números pares y otra que contenga los números impares utilizando list
# comprehensions.

ListaEntera=list(i for i in range(1,10))
print(list(ListaEntera))
ListaImpar=list(elemento for elemento in ListaEntera if elemento%2!=0)
print(list(ListaImpar))
ListaPar=list(elemento for elemento in ListaEntera if elemento%2==0)
print(list(ListaPar))
