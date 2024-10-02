from enum import Enum
import random

class Caracteristica(Enum):
    ATAQUE = "ataque"
    VIDA = "vida"
    DEFENSA = "defensa"

class CajaSorpresa:
    def __init__(self):
        self.__caracteristica = random.choice(list(Caracteristica))
        self.__valor = random.randint(0,10)

    def get_caracteristica(self):
        return self.__caracteristica

    def obtenerValor(self) -> int:
        return self.__valor