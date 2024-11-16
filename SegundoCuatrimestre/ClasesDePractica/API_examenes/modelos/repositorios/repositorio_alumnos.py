from modelos.entidades.alumno import Alumno
import json

class RepositorioAlumno:
    __ruta_archivo = "datos/alumnos.json"

    def __init__(self):
        self.__alumnos = self.__cargarTodos()

    def __cargarTodos(self)->list:
        #leer todo el contenido del archivo
        #convertirlo en lista de diccinoarios
        #convertir la lista de diccionarios en lista de objetos Alumno
        lista_objetos = []
        try:
            lista_dicc = []
            with open(RepositorioAlumno.__ruta_archivo, "r", encoding="UTF-8") as archivo:
                diccionarioDatos = json.load(archivo)
            lista_dicc = diccionarioDatos["alumnos"]
            Alumno.establecerUltimoID(diccionarioDatos["ultimoID"])
            for dicc in lista_dicc:
                lista_objetos.append(Alumno.fromDiccionario(dicc))
        except:
            print("Error al abrir el archivo alumnos.json")
        return lista_objetos
    
    def __guardarTodos(self):
        try:
            with open(RepositorioAlumno.__ruta_archivo, "w", encoding="UTF8") as archivo:
                lista_dic = []
                for alumno in self.__alumnos:
                    lista_dic.append(alumno.toDiccionario())
                diccionarioDatos ={
                    "ultimoID": Alumno.obtenerUltimoID(),
                    "alumnos": lista_dic
                }
                json.dump(diccionarioDatos, archivo)
        except:
            print("error guardando los datos de los alumnos")

    def obtenerTodos(self)->list:
        return self.__alumnos
    
    #VALIDACIONES!!
    def existeAlumnoConLegajo(self, legajo:int)-> bool:
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                return True
        return False
    
    def agregar(self, alumno:Alumno):
        if not self.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            self.__alumnos.append(alumno)
            self.__guardarTodos()
            return True
        else:
            return False
    
    def agregarDesdeDiccionario(self, dicc:dict):
        if not self.existeAlumnoConLegajo(dicc["legajo"]):
            alumno = Alumno.fromDiccionario(dicc)
            self.agregar(alumno)
   
    def obtenerAlumnoPorLegajo(self, legajo:int)->Alumno:
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                return alumno
        return None

    def modificarLegajoPorDatosIndividuales(self, legajo:int, apellido:str, nombre:str):
        #buscar el alumno a modificar
        alum = self.obtenerAlumnoPorLegajo(legajo)
        #reemplazar nombre y apellido
        if alum is not None:
            alum.establecerApellido(apellido)
            alum.establecerNombre(nombre)
            #guardar
            self.__guardarTodos()
        
    def modificarLegajoPorObjeto(self, alumno:Alumno):
        if self.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            alumno_a_modificar = self.obtenerAlumnoPorLegajo(alumno.obtenerLegajo())
            alumno_a_modificar.establecerApellido(alumno.obtenerApellido())
            alumno_a_modificar.establecerNombre(alumno.obtenerNombre())
            self.__guardarTodos()

    def eliminarPorLegajo(self, legajo:int)->bool:
        for alum in self.__alumnos:
            if legajo == alum.obtenerLegajo():
                self.__alumnos.remove(alum)
                self.__guardarTodos()
                return True
        return False