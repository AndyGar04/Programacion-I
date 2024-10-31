# 5. Escriba un programa que permita cargar una lista de alumnos junto con su nota del
# parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
# de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
# aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
# (el resultado no se almacena, se calcula):
# ALUMNOS PARCIAL RESULTADO
# Smith, Juan 70 Aprobado
# Suárez, María 35 Desaprobado

Notas=dict()
bandera=True
cont=0

while bandera:
    rta=int(input("¿Desea cargar un alumno? 1.Si 2.No"))
    if rta==1:
        Notas["nombre",cont]=input("Dame el nombre del alumno")
        Notas["nota",cont]=int(input("Dame la nota del alumno"))
        if (Notas["nota",cont]<40):
            Notas["AoD",cont]="Desaprobado"
        else:
            Notas["AoD",cont]="Aprobado"  
        cont+=1      
    elif rta==2:
        print("Joya, gracias")
        bandera=False
    else:
        print("Ingresaste un valor invalido")    

print(Notas)