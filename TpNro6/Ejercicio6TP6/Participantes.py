"""
Un club de deportes está organizando un torneo de atletismo, y nos pide que le
ayudemos a gestionar la información de los participantes y las disciplinas. El sistema
debe permitir registrar a los participantes y las disciplinas en las que compiten.

Cada Participante tiene un nombre, una edad y una nacionalidad.
Un Participante puede competir en varias Disciplinas.

"""

class Participante:
    
    def __init__(self, nombre:str,edad:int,nacionalidad:str):
        self.__nombre=nombre
        self.__edad=edad
        self.__nacionalidad=nacionalidad
        disciplina=list['Disciplina']
        
    #Consultas
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerNacionalidad(self)->str:
        return self.__nacionalidad
    
    def establecerNombre(self, nombre:str):
        self.__nombre=nombre
        
    def establecerEdad(self,edad:int):
        self.__edad=edad    
        
    def establecerNacionalidad(self, nacionalidad:str):
        self.__nacionalidad=nacionalidad        
        