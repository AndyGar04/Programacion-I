from classVehiculo import Vehiculo

class Auto(Vehiculo):
    VALOR_PUERTA = 50
    def __init__(self, patente:str, cantPuertas:int):
        super().__init__(patente)
        if not isinstance(cantPuertas, int) or cantPuertas<0:
            raise ValueError("La cantidad de puertas no debe ser negativa")
        self.__cantPuertas = cantPuertas
    
    def obtenerCosto(self) -> int:
        return Auto.VALOR_PUERTA * self.__cantPuertas
    
    def __str__(self):
        return f"{super().__str__()} cantidad de puertas: {self.__cantPuertas}"
    