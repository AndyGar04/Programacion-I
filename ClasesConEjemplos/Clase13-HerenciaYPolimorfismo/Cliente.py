from Persona import Persona
from Fecha import Fecha

class Cliente(Persona):
    def __init__(self, nombre:str = "", direccion = "", telefono:str = "", email:str = "", saldo:float=0.0, ciudad:str="Bahia Blanca", CUIT:str="", categoriaIVA:str="C"):
        super().__init__(nombre,direccion,telefono,email)
        if not isinstance(saldo, (int,float)) or saldo < 0:
            raise ValueError("El descuento debe ser un numero positivo.")
        if not isinstance(ciudad, str) or ciudad.isspace():
            raise ValueError("La ciudad debe ser un string valido.")
        if not isinstance(CUIT, str) or CUIT.isspace():
            raise ValueError("El CUIT debe ser un string valido.")
        if not isinstance(categoriaIVA,str)or categoriaIVA.isspace():
            raise ValueError("La categoria de IVA sebe ser un string valido")
        self.__saldo = saldo
        self.__ciudad = ciudad
        self.__CUIT = CUIT
        self.__categoriaIVA = categoriaIVA
        #Atributos privados, no hay subclases que necesiten accederlos
        
    def obtenerNombre(self)->str:
        return self._nombre
    
    def obtenerDireccion(self)->str:
        return self._direccion
    
    def obtenerSaldo(self)->float:
        return self.__saldo
    
    def obtenerCiudad(self)->str:
        return self.__ciudad
            