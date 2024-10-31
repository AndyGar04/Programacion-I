# 2. Escriba una función llamada EsBisiesto que permita ingresar un número de año y
# devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año
# es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre
# 400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por
# pantalla si la fecha es válida o no.

def EsBisiesto(anio):
    if (anio%4==0) and (anio%100!=0 or anio%4==0):
        Bisiesto=True
    else:
        Bisiesto=False

    return Bisiesto

dia=int(input("En que dia del año estamos en numero"))
mes=int(input("En que mes del año estamos en numero"))
anio=int(input("En que año estamos"))

#30 días, abril, junio, septiembre y noviembre.
#31 días, enero, marzo, mayo, julio, agosto, octubre y diciembre.
if (mes>0 and mes<13):
    if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        if (dia<=31 and dia>0):
            print("La fecha ingresada es correcta")
        else:
         print("La fecha ingresada no es correcta")
    elif (mes==4 or mes==6 or mes==9 or mes==11):
     if (dia<=30 and dia>0):
         print("La fecha ingresada es correcta")
     else:
         print("La fecha ingresada no es correcta")
    else:
     if (EsBisiesto(anio)):
           if (dia<=29 and dia>0):
                print("La fecha ingresada es correcta")
           else:
                print("La fecha ingresada no es correcta")                  
     else:
            if (dia<=28 and dia>0):
               print("La fecha ingresada es correcta")
            else:
                print("La fecha ingresada no es correcta")    
else:
    print("El mes es inexistente")