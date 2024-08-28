# 3. Escriba un programa que permita cargar las notas de exámenes, primero debe
# permitir ingresar por teclado la cantidad de notas que desea cargar, y luego
# cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e
# indicar en qué índice del arreglo se encuentra.

CantNotas=int(input("Dame la cantidad de notas a ingesar"))
Notas=list()

aux=0

for i in range(CantNotas):
    Nota=int(input("Dame una nota"))
    Notas.append(Nota)

print(Notas)

for i in range(len(Notas)):
    if (Notas[i]>aux):
        pos=i
        aux=Notas[i]

print(f"La nota más alta es el {Nota} y esta en la posicion {pos+1}")