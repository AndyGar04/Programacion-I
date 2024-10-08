from Empleado import Empleado
from Fecha import Fecha

class Ejecutivo(Empleado):
    viaticos = 1200
    vacaciones = 20
    def __init__(self, nombre:str = "", direccion:str = "", telefono:str = "", email:str = "", basico:float=0.0, cantHijos:int=0, fechaIngreso:Fecha=Fecha(1,1,2024), productividad:float=0.0, presupuesto:float=0.0):
        super().__init(nombre, direccion, telefono, email, basico, cantHijos, fechaIngreso)
        if not isinstance(productividad,(int,float)) or productividad<0:
            raise ValueError("La productividad debe ser un numero positivo")
        if not isinstance(presupuesto, (int, float)) or presupuesto<0:
            raise ValueError("El presupuesto debe ser un numero positivo")
        self.__productividad = productividad
        self.__presupuesto = presupuesto
        #Atributos privados porque no hay subclases que los requieran
        
        def obtenerProductividad(self)->float:
            return self.__productividad
        
        def obtenerPresupuesto(self)->float:
            return self.__presupuesto
        
        def diasVacaciones(self) -> int:
            """Retorna los dias de vacaciones de un ejecutivo"""
            return Ejecutivo.vacaciones
        
        
        
        