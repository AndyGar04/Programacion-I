from classVehiculo import Vehiculo
class Camion(Vehiculo):
    VALOR_POR_EJE = 100
    VALOR_TARA = 0.05
    def __init__(self, patente:str, cantEjes:int, tara:int):
        super().__init__(patente)
        if not isinstance(cantEjes, int) or cantEjes<=1:
            raise ValueError("El numero de ejes debe ser mayor a 1")
        if not isinstance(tara, int) or tara<=0:
            raise ValueError("La tara debe ser un numero positivo")
        self.__cantEjes = cantEjes
        self.__tara = tara

    def __str__(self)->str:
        return f"{super().__str__()} ejes: {self.__cantEjes}, tara: {self.__tara}"
    
    def obtenerCosto(self) -> float:
        return Camion.VALOR_POR_EJE * self.__cantEjes + Camion.VALOR_TARA * self.__tara