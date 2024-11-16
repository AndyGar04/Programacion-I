class Tema:
    @classmethod
    def fromDiccionario(cls, dic: dict)->"Tema":
        return cls(dic["numero"], dic["nombre"], dic["enunciado"])

    def __init__(self, numero:int, nombre:str, enunciado:str):
        #valdaciones!!!
        self.__numero = numero
        self.__nombre = nombre
        self.__enunciado = enunciado

    #consultas
    def obtenerNumero(self)->int:
        return self.__numero
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEnunciado(self)->str:
        return self.__enunciado
    
    #comandos
    # valdaciones!!
    def establecerNumero(self, num):
        self.__numero = num

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def establecerEnunciado(self, enu):
        self.__enunciado = enu

    def toDiccionario(self):
        return {
            "numero": self.__numero,
            "nombre": self.__nombre,
            "enunciado": self.__enunciado
        }