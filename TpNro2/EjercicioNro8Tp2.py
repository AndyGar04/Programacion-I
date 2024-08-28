# El mismo almacén del punto anterior almacena los datos del stock de productos en
# el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de
# producto; stock mínimo; stock real”. Escriba un programa, que a partir de
# información contenida en los archivos, genere otro archivo de texto, Compras.txt,
# conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo.
# Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y
# cargarle datos utilizando los códigos de los productos del archivo anterior. Ej:
# 100;50;60
# 102;50;20
# 135;20;15
# 138;20;20
# 140;10;8
# 201;20;30 

ruta_leer=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro2\txts\stock.txt"
archivo_lectura=open(ruta_leer,'r')

lista_articulos=list()

Buscar=True

for linea in archivo_lectura:
    lista=linea.split(";")
    lista_articulos.append({"CodigoProducto" : int(lista[0]), "StockMinimo" : int(lista[1]), "StockReal" : int(lista[2])})

print(lista_articulos)

ruta_escribir=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro2\txts\Compras.txt"
#archivo_escribir=open(ruta_escribir,'w')

Buscar=True

with open(ruta_escribir,'w') as archivo_escribir:
    for articulo in lista_articulos:
        if (articulo["StockMinimo"]>articulo["StockReal"]):
            archivo_escribir.write(f'{articulo["CodigoProducto"]};{articulo["StockMinimo"]};{articulo["StockReal"]}')
            archivo_escribir.write("\n")

print(lista_articulos)

archivo_escribir.close()
archivo_lectura.close()