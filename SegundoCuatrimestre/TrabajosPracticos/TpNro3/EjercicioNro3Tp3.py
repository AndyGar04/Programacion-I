# 3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas
# las líneas del archivo, utilizando list comprehensions.

ruta=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro3\Txts\datos.txt"
archivo_datos=open(ruta,'r')

Palabras=list()

Palabras=(palabra for linea in archivo_datos for palabra in linea.split())

print(list(Palabras))

archivo_datos.close()