# Un almacén guarda los códigos, los nombres de los productos y sus precios,
# respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer
# un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del
# archivo y buscar el precio de un artículo ingresado por teclado. Para probar el
# algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
# 100;arroz;10
# 102;fideos;5
# 135;lentejas;8
# 138;porotos;6
# 140;sal gruesa;5
# 201;aceite;20

ruta=r"c:\Users\estudiante\Desktop\Uni\CuatrimesNro2PProg\ProgramacionDosEne\TpNro2\txts\productos.txt"
archivo=open(ruta,'r')

lista_articulos=list()

Buscar=True

for linea in archivo:
    lista=linea.split(";")
    lista_articulos.append({"Codigo" : int(lista[0]), "Nombre" : lista[1], "Precio" : int(lista[2])})

print(lista_articulos)

archivo.close()

while Buscar:
    CodBus = input("Dame el nombre del producto buscado: ").strip()
    encontrado = False
    for articulo in lista_articulos:
        if (articulo["Nombre"].lower() == CodBus.lower()):
            print(f"¡Se encontró! Su valor es de {articulo['Precio']}")
            Buscar = False
            encontrado = True
    if (encontrado!=True):
        print("Vas a tener que seguir buscando")