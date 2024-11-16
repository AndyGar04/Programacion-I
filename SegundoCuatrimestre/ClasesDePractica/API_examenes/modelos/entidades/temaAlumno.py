from modelos.entidades.alumno  import Alumno
from modelos.entidades.tema import Tema

class TemaAlumno:
    @classmethod
    def fromDiccionario(cls, dic:dict)->"TemaAlumno":
        return cls(Alumno.fromDiccionario(dic["alumno"]), Tema.fromDiccionario(dic["tema"]))

    def __init__(self, alumno:Alumno, tema:Tema):
        #validaciones!!
        if not isinstance(alumno, Alumno):
            raise ValueError
        #.....
        self.__alumno  = alumno
        self.__tema = tema

    #consultas
    def obtenerAlumno(self)->Alumno:
        return self.__alumno
    
    def obtenerTema(self)->Tema:
        return self.__tema

    #comandos
    #Validaciones!!
    def establecerAlumno(self, alumno:Alumno):
        if not isinstance(alumno, Alumno):
            raise ValueError
        self.__alumno = alumno

    def establecerTema(self, tema:Tema):
        self.__tema=tema

    def toDiccionario(self):
        return {
            "alumno": self.__alumno.toDiccionario(),
            "tema": self.__tema.toDiccionario()
        }