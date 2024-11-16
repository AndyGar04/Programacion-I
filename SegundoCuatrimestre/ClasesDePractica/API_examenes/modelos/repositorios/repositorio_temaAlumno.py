from modelos.entidades.alumno import Alumno
from modelos.entidades.tema import Tema
from modelos.entidades.temaAlumno import TemaAlumno
import json
import random
import os

# class ExamenesDisponibles
class RepositorioTemasAlumnos:
    __ruta_archivo ="datos/temaalumno.json"

    def __init__(self):
        self.__temasAlumnos = self.__cargarTodos()

    def __cargarTodos(self)->list:
        lista_dicc=[]
        lista_obj = []
        try:
            with open(RepositorioTemasAlumnos.__ruta_archivo, "r", encoding="UTF-8") as archivo:
                lista_dicc = json.load(archivo)
        except:
            print("error cargando de archivo temaalumnos.json")

        if len(lista_dicc)>0:            
            for dicTemaAlumno in lista_dicc:
                lista_obj.append(TemaAlumno.fromDiccionario(dicTemaAlumno))
        else:
                #combinacion aleatoria de temas con alumnos
            from modelos.repositorios.repositorios import obtenerRepoAlumnos, obtenerRepoTemas
            repo_alumnos = obtenerRepoAlumnos()
            repo_temas = obtenerRepoTemas()
            if len(repo_alumnos.obtenerTodos())>0 and len(repo_temas.obtenerTodos())>0:
                for alumno in repo_alumnos.obtenerTodos():
                    lista_obj.append(TemaAlumno(alumno, random.choice(repo_temas.obtenerTodos())))
                    #alternatva
                    # num_random = random.randint(1,5)
                    # lista_obj.append(alumno, repo_temas.obtenerTemaPorNumero(num_random))           
                self.__guardarCombinacion(lista_obj)
        return lista_obj

    def __guardarCombinacion(self, lista_objetos):
        lista_dicc = []
        for temaAlumno in lista_objetos:
            if isinstance(temaAlumno, TemaAlumno):
                lista_dicc.append(temaAlumno.toDiccionario())
        with open(RepositorioTemasAlumnos.__ruta_archivo, "w", encoding="UTF-8") as arch:
            json.dump(lista_dicc, arch)

    def __guardarTodos(self):
        lista_dicc = []
        for temaAlumno in self.__temasAlumnos:
            if isinstance(temaAlumno, TemaAlumno):
                lista_dicc.append(temaAlumno.toDiccionario())
        with open(RepositorioTemasAlumnos.__ruta_archivo, "w", encoding="UTF-8") as arch:
            json.dump(lista_dicc, arch)

    def obtenerPorAlumnoID(self, alumnoID:int)->TemaAlumno:
        for temaAlumno in self.__temasAlumnos:
            if temaAlumno.obtenerAlumno().obtenerID() == alumnoID:
                return temaAlumno            
        return None
    
    def generarParaAlumno(self, legajo:int):
        #from modelos.repositorios.repositorios import obtenerRepoAlumnos
        #from modelos.repositorios.repositorios import obtenerRepoTemas
        #buscar el alumno por el legajo
        #crear un TemaAlumno asgnando aleatoriamente el tema
        #guardar todo
        #retornar el objeto creado TemaAlumno
        pass