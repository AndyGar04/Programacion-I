from classVehiculo import Vehiculo
class Colectivo(Vehiculo):
    VALOR_PASAJERO = 60
    def __init__(self, patente:str, cantPasajeros:int):
        super().__init__(patente)
        if not isinstance(cantPasajeros, int) or cantPasajeros<0:
            raise ValueError("Los pasajeros deben ser un numero positivo")
        self.__cantPasajeros=cantPasajeros

    def obtenerCosto(self) -> int:
        return Colectivo.VALOR_PASAJERO * self.__cantPasajeros
    
    def __str__(self):
        return f"{super().__str__()} cantidad de pasajeros: {self.__cantPasajeros}"