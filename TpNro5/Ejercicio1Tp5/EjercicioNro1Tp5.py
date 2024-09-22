"""
1) En un videojuego se modelan atletas que tienen la capacidad de entrenar para
mejorar su destreza o descansar. Cada atleta tiene un nivel de energía que
comienza en un valor máximo predeterminado al crearse. Cuando un atleta entrena,
consume 5 unidades de energía, y cuando descansa recupera 20. Cada cinco
entrenamientos el atleta mejora en 1 punto su destreza, que al crearse comienza
con su valor en el mínimo predeterminado. La
Los servicios mismaDestrezaQue y esMejorQue comparan a los atletas por su nivel
de destreza.

a) Implemente el siguiente diagrama de acuerdo a la especificación,
encapsulando atributos y comportamiento. Debe implementar también los
comandos y consultas triviales que no figuran en el diagrama.
"""

class Atletas:
    #Atributos de la clase
    __MAX_VALOR=100
    __MIN_VALOR=0

    #Atributos de la instancia
    def __init__(self, nombre:str, energia:int=__MAX_VALOR,destreza:int=__MIN_VALOR):
        self.__nombre=nombre
        self.__energia=energia
        self.__destreza=destreza
        self.__entrenamientos=0

    #Comandos
    def Entrenar(self)->int:
        if self.__energia - 5 > Atletas.__MIN_VALOR:
            self.__energia -= 5
            self.__entrenamientos+=1
            if (self.__entrenamientos==5):
                self.__destreza+=1
                self.__entrenamientos=0
        else:
            print("El atleta trato de entrenar pero estaba muy cansado...")
            self.__energia=Atletas.__MIN_VALOR
        return self.__energia, self.__destreza, self.__entrenamientos

    def Descansar(self)->int:
        if(self.__energia + 20 > Atletas.__MAX_VALOR):
            self.__energia=Atletas.__MAX_VALOR
        else:
            self.__energia+=20
        return self.__energia

    def establecerNombre(self, nombre:str):
        self.__nombre=nombre

    def establecerDestreza(self,destreza:int):
        self.__destreza=destreza

    def establecerEnergia(self,energia:int):
        self.__energia=energia        

    #Consultas

    def obtenerDestreza(self)->int:
        return self.__destreza

    def obtenerEnergia(self)->int:
        return self.__energia

    def obtenerNombre(self)->str:
        return self.__nombre        

    def mismaDestrezaQue(self,otroAtleta:"Atleta")->bool:
        if (self.__destreza==(otroAtleta.obtenerDestreza())):
            return True
        else:
            return False

    def mayorDestrezaQue(self,otroAtleta:"Atleta")->bool:
        if (self.__destreza>(otroAtleta.obtenerDestreza())):
            return True
        else:
            return False            

                     
