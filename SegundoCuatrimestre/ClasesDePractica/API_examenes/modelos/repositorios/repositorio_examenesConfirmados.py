from modelos.entidades.alumno import Alumno
from modelos.entidades.tema import Tema
from modelos.entidades.temaAlumno import TemaAlumno
import json
import random
import os

# class ExamenesDisponibles
class RepositorioExamenesConfirmados:
    __ruta_archivo ="datos/examenesConfirmados.json"

    def __init__(self):
        self.__examenesConfirmados = self.__cargarTodos()

    def __cargarTodos(self)->list:
        lista_dicc=[]
        lista_obj = []
        try:
            with open(RepositorioExamenesConfirmados.__ruta_archivo, "r", encoding="UTF-8") as archivo:
                lista_dicc = json.load(archivo)
        except:
            print("error cargando de archivo temaalumnos.json")

        if len(lista_dicc)>0:            
            for dicTemaAlumno in lista_dicc:
                lista_obj.append(TemaAlumno.fromDiccionario(dicTemaAlumno))
        return lista_obj

    def __guardarTodos(self):
        lista_dicc = []
        for temaAlumno in self.__examenesConfirmados:
            if isinstance(temaAlumno, TemaAlumno):
                lista_dicc.append(temaAlumno.toDiccionario())
        with open(RepositorioExamenesConfirmados.__ruta_archivo, "w", encoding="UTF-8") as arch:
            json.dump(lista_dicc, arch)

    def obtenerTodos(self):
        return self.__examenesConfirmados

    def obtenerPorAlumnoID(self, alumnoID:int)->TemaAlumno:
        for temaAlumno in self.__examenesConfirmados:
            if temaAlumno.obtenerAlumno().obtenerID() == alumnoID:
                return temaAlumno            
        return None
    
    def agregar(self, examen:TemaAlumno):
        self.__examenesConfirmados.append(examen)
        self.__guardarTodos()