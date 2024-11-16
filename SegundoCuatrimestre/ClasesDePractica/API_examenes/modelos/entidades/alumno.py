class Alumno:
    __ultimoID=0

    @classmethod
    def generarID(cls)-> int:
        cls.__ultimoID += 1
        return cls.__ultimoID
    
    @classmethod
    def obtenerUltimoID(cls)->int:
        return cls.__ultimoID
    
    @classmethod
    def establecerUltimoID(cls, id):
        #valdaciones
        if not isinstance(id, int) or id<0:
            raise ValueError
        cls.__ultimoID = id

    @classmethod
    def fromDiccionario(cls, dicc:dict)->"Alumno":
        if "id" in dicc:
            return cls(dicc["legajo"], dicc["apellido"], dicc["nombre"], dicc["id"])
        else:
            return cls(dicc["legajo"], dicc["apellido"], dicc["nombre"])
    
    #metodos de instancia
    def __init__(self, legajo:int, apellido:str, nombre:str, id:int=None):
        if not isinstance(legajo, int) or legajo<0:
            raise ValueError
        if not isinstance(apellido, str):
            raise ValueError
        if not isinstance(nombre, str):
            raise ValueError
        if id != None:
            self.__id = id
        else:
            self.__id = Alumno.generarID()
        self.__legajo = legajo
        self.__nombre = nombre
        self.__apellido = apellido

    #consultas
    def obtenerID(self)->int:
        return self.__id
    
    def obtenerLegajo(self)->int:
        return self.__legajo
    
    def obtenerApellido(self)->str:
        return self.__apellido
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def toDiccionario(self)->dict:
        # dic = {
        #     "id": self.__id,
        #    "legajo":self.__legajo,
        #    "apellido":self.__apellido,
        #    "nombre":self.__nombre
        #    }
        return {
            "id": self.__id,
           "legajo":self.__legajo,
           "apellido":self.__apellido,
           "nombre":self.__nombre
           }

    #comandos
    def establecerLegajo(self, legajo):
        self.__legajo = legajo

    def establecerNombre(self, nombre):
        self.__nombre = nombre
    
    def establecerApellido(self, apellido):
        self.__apellido = apellido