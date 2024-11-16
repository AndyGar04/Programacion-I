from modelos.entidades.tema import Tema
import json 

class RepositorioTema:
    __ruta_archivo = "datos/temas.json"

    def __init__(self):
        self.__temas = self.__cargarTodos()
#VALIDACIONES!!
    def __cargarTodos(self)->list:
        lista_dicc=[]
        try:
            with open(RepositorioTema.__ruta_archivo, "r", encoding="UTF-8") as archivo:
                lista_dicc = json.load(archivo)
        except:
            print("error cargando de archivo temas")
        lista_obj = []
        for dicTema in lista_dicc:
            lista_obj.append(Tema.fromDiccionario(dicTema))
        return lista_obj
    
    def __guardarTodos(self):
        lista_dicc =[]
        for tema in self.__temas:
            lista_dicc.append(tema.toDiccionario())
        try:
            with open(RepositorioTema.__ruta_archivo, "w", encoding="UTF-8") as archivo:
                json.dump(lista_dicc, archivo)
        except Exception as e:
            print("error guardando en temas.json\n" + str(e))

    def existeTemaNumero(self, numero:int):
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                return True
        return False

    def agregar(self, tema_nuevo:Tema):
        if not self.existeTemaNumero(tema_nuevo.obtenerNumero()):
            self.__temas.append(tema_nuevo)
            self.__guardarTodos()
    
    def obtenerTodos(self):
        return self.__temas
    
    def obtenerTemaPorNumero(self, numero):
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                return tema
        return None
    
    def eliminar(self, numero:int):
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                self.__temas.remove(tema)
                self.__guardarTodos()
                return True
        return False
    
    def modificarPorNumero(self, numero:int, nombre:str, enunciado:str):
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                tema.establecerNombre(nombre)
                tema.establecerEnunciado(enunciado)
                self.__guardarTodos()
                return True
        return False