"""
b. implementar una clase tester que cree un objeto de clase Automovil, y que
pida al usuario la cantidad de iteraciones a realizar, luego para cada iteración
deberá generar un número aleatorio entre 0 y 3 que determinará la operación
a realizar:
● 0: acelerar(20)
● 1: desacelerar(15)
● 2: frenarPorCompleto()
● 3: calcularMinutosParaLlegar(50)
En cada iteracion se debe mostrar el valor que se modificará, la acción a
realizar y el valor modificado luego de la acción. Por ejemplo, si tocó el valor
0 muestra: “velocidad = 100, acelerar, velocidad actual = 120”. En el caso del
calculo del tiempo para llegar debe mostrar el tiempo para llegar.
"""    

from EjercicioNro4Tp4 import Automovil
import random

class TestEjercicio4Tp4:
    @staticmethod
    
    def test():
        marca=input("Dame la marca")
        modelo=input("Dame un modelo")
        anio=int(input("Dame el anio"))
        velocidadMaxima=float(input("Dame la velocidad maxima"))
        auto_1=Automovil(marca,modelo,anio,velocidadActual,0)

        cantidad=int(input("Dame una cantidad de iteraciones"))

        for i in range(cantidad):
            numero = random.randint(0, 3)
            if (numero==0):
                print(f"La velocidad actual es de {auto_1.obtenerVelocidadActual()}km/h, aceleraremos un poco")
                auto_1.acelerar(20)
                print(f"Ahora vamos a {auto_1.obtenerVelocidadActual()}km/h")
            elif (numero==1):
                print(f"La velocidad actual es de {auto_1.obtenerVelocidadActual()}, desaceleraremos un poco")  
                auto_1.desacelerar(15)
                print(f"Ahora vamos a {auto_1.obtenerVelocidadActual()}km/h")
            elif(numero==2):
                print(f"Vamos a frenar, ibamos a {auto_1.obtenerVelocidadActual()}km/h")
                auto_1.frenarPorCompleto()
            elif(numero==3):
                print(f"A la velocidad que vamos tardaremos {auto_1.calcularMinutosParaLlegar(50)} mins")
                
if __name__ == "__main__":
    TestEjercicio4Tp4.test()




