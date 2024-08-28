# 8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los
# elementos únicos utilizando list comprehensions

listaDupli=[2,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10]

lista=list()

lista=(set(elemento for elemento in listaDupli))

print(list(lista))