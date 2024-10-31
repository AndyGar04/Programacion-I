"""
Se requiere un programa que modele el concepto de un Automóvil. Para simplificar
consideraremos que un automóvil tiene solamente los siguientes atributos:
Marca: el nombre del fabricante.
Modelo: nombre del modelo.
Año: año de fabricación.
Velocidad máxima: velocidad máxima soportada por el vehículo en km/h.
Velocidad actual: velocidad del vehículo en un momento dado en km/h.
"""

# a. implementar la clase en python

class Automovil:

    #constructor
    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float,velocidadActual:float):
        self.__marca=marca
        self.__modelo=modelo
        self.__anio=anio
        self.__velocidadMaxima=velocidadMaxima
        self.__velocidadActual=velocidadActual

    #comandos    
    def establecerMarca(self,marca:str):
        self.__marca=marca

    def establecerModelo(self, modelo:str):
        self.__modelo=modelo

    def establecerAnio(self, anio:int):
        self.__anio=anio

    def establecerVelocidadMaxima(self, velocidadMaxima:float):
        self.__velocidadMaxima=velocidadMaxima

    def establecerVelocidadActual(self, velocidadActual:float):
        self.__velocidadActual=velocidadActual

    """
        Es importante tener en cuenta que no se debe acelerar más allá de la velocidad
        máxima permitida para el automóvil. De igual manera, tampoco es posible
        desacelerar a una velocidad negativa. Si se cumplen estos casos, se debe
        establecer la velocidad en el límite correspondiente y mostrar por pantalla un
        mensaje.
    """

    def acelerar(self, incrementoVelocidad:float):
        if (self.__velocidadActual+incrementoVelocidad)>self.__velocidadMaxima:
            print(f"Pudo acelerarse hasta {self.__velocidadMaxima} km/h")
        else:
            self.__velocidadActual=self.__velocidadActual+incrementoVelocidad
            print(f"Se acelero hasta {self.__velocidadActual} km/h")

    def desacelerar(self, decrementoVelocidad:float):
        if (self.__velocidadActual-decrementoVelocidad)<=0:
            print("El auto desacelero tanto que freno...")
            self.__velocidadActual=0
        else:    
            self.__velocidadActual=self.__velocidadActual-decrementoVelocidad    
            print(f"Se bajo la velocidad hasta {self.__velocidadActual}")           

    def frenarPorCompleto(self):
        self.__velocidadActual=0
        return self.__velocidadActual

    #consultas    
    def obtenerMarca(self)->str:
        return self.__marca

    def obtenerModelo(self)->str:
        return self.__modelo

    def obtenerAnio(self)->int:
        return self.__anio

    def obtenerVelocidadActual(self)->float:
        return self.__velocidadActual

    def obtenerVelocidadMaxima(self)->float:
        return self.__velocidadMaxima

    """
        El tiempo estimado en horas se calcula como el cociente entre la distancia en 
        kilómetros a recorrer y la velocidad actual (en km/h), multiplicando este valor por 60
        obtenemos la cantidad de minutos. Considerar el caso especial cuando el auto se
        encuentre detenido, en este caso mostrar un mensaje indicando que “el auto está
        detenido y no se puede calcular el tiempo para llegar”.
    """    

    def calcularMinutosParaLlegar(self, distanciaKM:float)->int:
        tiempoParaLlegar=0
        if (self.__velocidadActual<=0):
            print("El auto se encuentra detenido es imposible calcular el tiempo de llegada")
        else:
           tiempoParaLlegar=int((distanciaKM/self.__velocidadActual)*60)   
        
        return tiempoParaLlegar   




