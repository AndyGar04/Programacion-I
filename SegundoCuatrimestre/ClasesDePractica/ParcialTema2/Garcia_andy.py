"""
Un gimnasio desea mantener información de las actividades que se realizan, y en particular de las clases que 
dictan sus entrenadores (zumba, spinning, etc..). Le interesa mantener la información tanto de los entrenadores 
como de las clases, y éstas pueden ser grupales o individuales. Las clases grupales tienen un limite máximo de 
participantes.
"""

from abc import ABC, abstractmethod

class Clase(ABC):
    
    #Constructor
    def __init__(self, nombre:str, duracion:int, horaInicio:str, horaFin:str, precio:float):
        #Escribimos las validaciones, con el objetivo de tener un constructor con datos correctos
        if not isinstance(nombre, str) or nombre.isspace():
            raise ValueError("El nombre debe ser un string")
        else:
            self._nombre=nombre
        
        if not isinstance(duracion, int) or duracion<0:
            raise ValueError("La duracion debe ser un numero entero positivo")
        else:
            self._duracion=duracion
        
        if not isinstance(horaInicio, str) or horaInicio.isspace():
            raise ValueError("La hora de inicio debe ser un string")
        else:
            self._horaInicio=horaInicio
            
        if not isinstance(horaFin, str) or horaFin.isspace():    
            raise ValueError("La hora de finalizacion debe ser un string")
        else:
            self._horaFin=horaFin
            
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un numero positivo o 0")
        else:
            self._precio=precio
            
    def establecerEntrenador():
        pass
    
    @abstractmethod
    def hayLugar(self)->bool:
        pass
    
    @abstractmethod
    def obtenerDescripcion(self)->str:
        pass
    
"""
Clase, clase grupal
"""                
        
class ClaseGrupal(Clase):
    
    #Constructor heredado, ademas agregaremos los atributos de esta subclase
    def __init__(self, nombre:str, duracion:int, horaInicio:str, horaFin:str, precio:float, maxParticipantes:int, cantInscriptos:int):
        super().__init__(nombre, duracion, horaInicio, horaFin, precio)
        #Escribimos las validaciones, con el objetivo de tener un constructor con datos correctos
        if not isinstance(maxParticipantes, int) or maxParticipantes<=0:
            raise ValueError("El numero maximo de participantes debe ser entero mayor a 0")
        else:
            self.__maxParticipantes=maxParticipantes
            
        if not isinstance(cantInscriptos, int) or cantInscriptos<0:
            raise ValueError("La cantidad de inscriptos debe ser un entero positivo")
        else:
            self.__cantInscriptos=cantInscriptos
    
    def registrarInscripto(self):
        if self.hayLugar():
            #Si la cantidad de inscriptos es menor a la cantidad maxima de inscriptos significa que se puede anotar
            self.__cantInscriptos+=1
            print("Se pudo inscribir")
        else:
            print("No se pudo inscribir la clase esta llena")    
            
            
    def hayLugar(self)->bool:
        hayLugar=False
        if self.__maxParticipantes > self.__cantInscriptos:
            #Si la cantidad maxima de participantes es mayor a la cantidad de inscriptos significa que hay lugar
            hayLugar=True
        else:
            hayLugar=False
            
        return hayLugar
    
    def obtenerDescripcion(self)->str:
        return f"Nombre:{self._nombre}, Duracion:{self._duracion}, Hora de inicio:{self._horaInicio}, Hora de finalizacion:{self._horaFin}, Precio:{self._precio}, Maxima cantidad de participantes:{self.__maxParticipantes}, Cantidad de inscriptos:{self.__cantInscriptos}"
    
"""
Clase, clase individual
"""
    
class ClaseIndividual(Clase):
    #Constructor heredado, ademas agregaremos los atributos de esta subclase
    def __init__(self, nombre:str, duracion:int, horaInicio:str, horaFin:str, precio:float, ocupada:bool):
        super().__init__(nombre, duracion, horaInicio, horaFin, precio)
        #Escribimos las validaciones, con el objetivo de tener un constructor con datos correctos
        if not isinstance(ocupada, bool):
            raise ValueError("La variable ocupada debe ser un booleano")
        else:
            self.__ocupada=ocupada
            
    def hayLugar(self)->bool:
        hayLugar=False
        if self.__ocupada:
            hayLugar=False
        else:
            hayLugar=True
            
        return hayLugar
    
    def establecerInscripto(self):
        if self.hayLugar():
            self.__ocupada=True
        else:
            self.__ocupada=False
            
    def obtenerDescripcion(self)->str:
        return f"Nombre:{self._nombre}, Duracion:{self._duracion}, Ocupada:{self.__ocupada}"      
    
"""
Clase, Entrendador
"""

class Entrenador():
    
    def __init__(self, DNI:int, nombre:str, apellido:str, mail:str, especialidad:str):
        pass
    
    def toString(self):
        pass                