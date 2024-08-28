# 6. Escriba un programa que permita leer de un archivo distancias.txt (cada renglón
# tiene una distancia válida) las distancias recorridas por el vehículo de una empresa,
# luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y
# todas las distancias mayores al promedio.
# Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor
# son: … , … , …. , …. “

ruta=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro2\txts\Ej6Tp2.txt"
archivo=open(ruta,'r')

Enteros=list()
SumTotal=0

for linea in archivo:
    Numero=int(linea)
    SumTotal=SumTotal+Numero
    Enteros.append(Numero)

Promedio=(SumTotal/len(Enteros))

print(f"La distancia promedio de los viajes es {Promedio} y los viajes con distancia mayor", end=" ")

for i in range(len(Enteros)):

    if (Enteros[i]>Promedio):
        print(f"{Enteros[i]}", end=",")

archivo.close()
