from classVehiculo import Vehiculo

class Moto(Vehiculo):
    VALOR_MOTO=0
    def __init__(self, patente:str):
        super().__init__(patente)

    def obtenerCosto(self) -> int:
        return Moto.VALOR_MOTO
    