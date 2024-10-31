"""
2. Una organización desea mantener información básica sobre sus empleados para
calcular los sueldos, para ello diseñó la siguiente clase:

a. implementar en python la clase Empleado.

"""    

class Empleado:
    #atributos de la instancia, constructor 

    def __init__(self, legajo:int, horasTrabajadasMes:int=0, valorHora:float=0.0):
        self.__legajo=legajo
        self.__horasTrabajadasMes=horasTrabajadasMes
        self.__valorHora=valorHora

    #Comandos
    def establecerHorasTrabajadas(self, cantHoras: int):
        self.__horasTrabajadasMes = cantHoras 

    def establecerValorHora(self, valorHora:float):
        self.__valorHora=valorHora 

    def obtenerLegajo(self)->int:
        return self.__legajo

    def obtenerHorasTrabajadas(self)->int:
        return self.__horasTrabajadasMes

    def obtenerValorHora(self)->float:
        return self.__valorHora

    def obtenerSueldo(self)->float:
        Sueldo=(self.__horasTrabajadasMes)*(self.__valorHora)
        return Sueldo           

