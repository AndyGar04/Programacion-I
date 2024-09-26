"""
    De los libros se mantiene el nombre, su
    autor, la editorial y la categoría a la que pertenecen, que puede ser A, B o C. De los
    socios se mantiene el nombre, la fecha de nacimiento y la fecha de penalización (si
    es que hubiere) indicando hasta qué fecha no puede retirar libros
"""

from Fecha import Fecha
from Ej6Prestamo import Prestamo
from Ej6Socio import Socio

class Libro:

    #Atributos

    #Contructor

    def __init__ (nombre:str,autor:str,editorial:str,categoria:char):
        self.__nombre=nombre
        self.__autor=autor
        self.__editorial=editorial
        self.__categoria=categoria

    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerAutor(self)->str:
        return self.__autor

    def obtenerEditorial(self)->str:
        return self.__editorial

    def obtenerCategoria(self)->char:
        return self.__categoria                