import random

class RobotDeBatalla:
    #atributos de clase
    __MAX_VIDA=100
    __MIN_VIDA=0
    __MAX_ATAQUE_DEFENSA=50
    __MIN_ATAQUE_DEFENSA=0
    __MAX_ENERGIA=100
    __MIN_ENERGIA=0

    def __init__(self,nombre:str):
        self.__nombre = nombre
        self.__vida = RobotDeBatalla.__MAX_VIDA
        self.__energia = RobotDeBatalla.__MAX_ENERGIA
        self.__ataque = random.randint(20, RobotDeBatalla.__MAX_ATAQUE_DEFENSA)
        self.__defensa = random.randint(10, RobotDeBatalla.__MAX_ATAQUE_DEFENSA)

    #consultas
    def obtenerVida(self)-> int:
        return self.__vida
    
    def obtenerNombre(self)-> str:
        return self.__nombre
    
    def obtenerDefensa(self)-> int:
        return self.__defensa
    
    def obtenerAtaque(self)-> int:
        return self.__ataque
    
    def obtenerEnergia(self)-> int:
        return self.__energia
    
    def estaVivo(self)-> bool:
        return self.__vida > 0
    
    #comandos
    def establecerEnergia(self, valor: int):
        """Establece el valor en energia"""
        if self.estaVivo():
            if valor>= RobotDeBatalla.__MIN_ENERGIA and valor <= RobotDeBatalla.__MAX_ENERGIA:
                self.__energia = valor
            else:
                raise ValueError("El valor de energia debe estar entre el minimo y el maximo permitido")

    def establecerAtaque(self, valor: int):
        if self.estaVivo():
            if RobotDeBatalla.__MIN_ATAQUE_DEFENSA <= valor <= RobotDeBatalla.__MAX_ATAQUE_DEFENSA:
                self.__ataque= valor

    def establecerDefensa(self, valor: int):
        if self.estaVivo():
            if RobotDeBatalla.__MIN_ATAQUE_DEFENSA <= valor <= RobotDeBatalla.__MAX_ATAQUE_DEFENSA:
                self.__defensa= valor

    def establecerVida(self, valor: int):
        if self.estaVivo():
            if RobotDeBatalla.__MIN_VIDA <= valor <= RobotDeBatalla.__MAX_VIDA:
                self.__vida= valor

    def establecerNombre(self, nombre: str):
        if self.estaVivo():
            self.__nombre = nombre

    def recargarEnergia(self):
        if self.estaVivo():
            self.__energia = RobotDeBatalla.__MAX_ENERGIA

    def atacar(self, otroRobot:"RobotDeBatalla"):
        if self.__energia - 5 > RobotDeBatalla.__MIN_ENERGIA:
            self.__energia  -= 5
            if self.estaVivo():
                #atacar al otro robot
                otroRobot.recibirDanio(self.__ataque)
             
        else:
            self.__energia = 0

    def recibirDanio(self, ataque: int):
        if self.estaVivo():
            if self.__defensa >= ataque:                
                self.__defensa = self.__defensa - ataque
            else:
                #defensa es < ataque
                if self.__defensa > RobotDeBatalla.__MIN_ATAQUE_DEFENSA:
                    danio = ataque - self.__defensa
                    self.__defensa = self.__defensa - (ataque - danio)
                    # sería lo mismo que:
                    # self.__defensa = RobotDeBatalla.__MIN_ATAQUE_DEFENSA
                    if self.__vida - danio >= RobotDeBatalla.__MIN_VIDA:
                        self.__vida = self.__vida - danio
                    else:
                        self.__vida = RobotDeBatalla.__MIN_VIDA
                else:
                    if self.__vida - ataque >= RobotDeBatalla.__MIN_VIDA :
                        self.__vida -= ataque
                    else:
                        self.__vida = RobotDeBatalla.__MIN_VIDA 
            if self.estaVivo():
                if self.__vida < self.__energia:
                    self.recargarEnergia()

    def __str__(self):
        return f"{self.__nombre} - vida: {self.__vida} - ataque: {self.__ataque} - defensa: {self.__defensa} - energia: {self.__energia}"

        