# 9. Un profesor almacenó los datos de los alumnos de su materia en un archivo
# alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas
# finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de
#  legajo.
# En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de
# legajo y nombre de cada uno.
# En ambos archivos los datos están separados por punto y coma ( ; ) .
# Desea escribir un programa para generar un archivo Promoción.txt con los apellidos
# y nombres de los alumnos que promocionan la materia, esto es, alumnos que el
# promedio de las tres notas supere los 7 puntos.
# El archivo debe quedar ordenado alfabéticamente


ruta_alumnostxt=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro2\txts\alumnos.txt"
archivo_alumnostxt=open(ruta_alumnostxt,'r')

lista_alumnostxt=list()
lista_legajo_promocion=list()

for alumnos in archivo_alumnostxt:
    lista=alumnos.split(";")
    lista_alumnostxt.append({"NroLegajo" : int(lista[0]), "Nota1" : int(lista[1]),"Nota2" : int(lista[2]),"Nota3" : int(lista[3])})

for alumnos in lista_alumnostxt:
    if (((alumnos["Nota1"]+alumnos["Nota2"]+alumnos["Nota3"])/3)>=7):
        lista_legajo_promocion.append(alumnos["NroLegajo"])       

print(lista_alumnostxt)
print(lista_legajo_promocion)

ruta_alumnosLtxt=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro2\txts\alumnosL.txt"
archivo_alumnosLtxt=open(ruta_alumnosLtxt,'r')

lista_alumnosnombre=list()

for alumnos in archivo_alumnosLtxt:
    lista=alumnos.split(";")
    lista_alumnosnombre.append({"NroLegajo" : int(lista[0]), "Nombre" : lista[1]})


ruta_promocion=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro2\txts\Promocion.txt"
archivo_promocion=open(ruta_promocion,'w')

lista_promocion=list()

for legajo in lista_legajo_promocion:
    NroLegajoPromocion=legajo
    for legajo2 in lista_alumnosnombre:
        if (NroLegajoPromocion==int(legajo2["NroLegajo"])):
            #lista_promocion.append({"NroLegajo" : int(legajo2["NroLegajo"])})   
            lista_promocion.append({"Nombre" : legajo2["Nombre"]})

print(lista_promocion)

with open(ruta_promocion,'w') as archivo_promocion:
    for aprobados in lista_promocion:
            archivo_promocion.write(f'{aprobados["Nombre"]}')
            archivo_promocion.write("\n")

archivo_alumnosLtxt.close()
archivo_alumnostxt.close()
archivo_promocion.close()

