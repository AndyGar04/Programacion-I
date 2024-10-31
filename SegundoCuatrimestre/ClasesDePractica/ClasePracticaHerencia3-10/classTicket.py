from classVehiculo import Vehiculo
from datetime import datetime
from Fecha import Fecha

class Ticket:
    def __init__(self, vehiculo: Vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("Se requiere un objeto de clase Vehículo")
        self.__vehiculo = vehiculo
        self.__fecha=Fecha(datetime.now().day, datetime.now().month, datetime.now().year)
        self.__hora = str(datetime.now().time())
        self.__valor = vehiculo.obtenerCosto()

    def __str__(self) -> str:
        return f"vehiculo: {self.__vehiculo} - fecha: {self.__fecha} - hora {self.__hora} - Valor: {self.__valor}"