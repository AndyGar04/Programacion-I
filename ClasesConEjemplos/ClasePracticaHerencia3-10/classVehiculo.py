class Vehiculo:
    def __init__(self, patente: str):
        if not isinstance(patente, str) or patente =="" or patente.isspace():
            raise ValueError("La patente debe ser string")
        self._patente = patente

    def obtenerPatente(self)->str:
        return self._patente
    
    def obtenerCosto()->None:
        return None
    
    def __str__(self)->str:
        return f"patente: {self._patente}"