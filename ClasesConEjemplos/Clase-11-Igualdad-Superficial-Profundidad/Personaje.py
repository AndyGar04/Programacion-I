from CajaSorpresa import CajaSorpresa
from CajaSorpresa import Caracteristica
from Arma import Arma

class Personaje:  
    # Atributos de clase  
    MAX_VIDA = 100  
    MAX_ATAQUE = 50  
    MAX_DEFENSA = 45  
    MIN_VIDA = 8  
    MIN_ATAQUE = 5  
    MIN_DEFENSA = 0  

    def __init__(self, nombre: str, ataque: int, defensa: int):  
        """  
        Inicializa un nuevo personaje.  

        Parámetros:  
        - nombre: El nombre del personaje.  
        - ataque: La cantidad de ataque del personaje.  
        - defensa: La cantidad de defensa del personaje.  
        """  
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():  
            raise ValueError("El nombre debe ser un string válido.")  
        if not isinstance(ataque, int) or ataque < Personaje.MIN_ATAQUE or ataque > Personaje.MAX_ATAQUE:  
            raise ValueError(f"El ataque debe ser un número entero entre {Personaje.MIN_ATAQUE} y {Personaje.MAX_ATAQUE}.")  
        if not isinstance(defensa, int) or defensa < Personaje.MIN_DEFENSA or defensa > Personaje.MAX_DEFENSA:  
            raise ValueError(f"La defensa debe ser un número entero entre {Personaje.MIN_DEFENSA} y {Personaje.MAX_DEFENSA}.")  
        
        self.__nombre = nombre  
        self.__vida = Personaje.MAX_VIDA  
        self.__ataque = ataque  
        self.__defensa = defensa  
        self.__arma = None  

    def obtenerNombre(self) -> str:  
        """Devuelve el nombre del personaje."""  
        return self.__nombre  

    def obtenerVida(self) -> int:  
        """Devuelve la vida del personaje."""  
        return self.__vida  

    def obtenerAtaque(self) -> int:  
        """Devuelve el ataque del personaje."""  
        return self.__ataque  

    def obtenerDefensa(self) -> int:  
        """Devuelve la defensa del personaje."""  
        return self.__defensa  

    def obtenerArma(self):  
        """Devuelve el arma del personaje."""  
        if self.__arma is None:
            print("Este personaje no tiene un arma.")
        else:
            return self.__arma

    def __str__(self):  
        """Devuelve una representación de string del personaje."""  
        return f"Nombre: {self.__nombre}, Vida: {self.__vida}, Ataque: {self.__ataque}, Defensa: {self.__defensa}, Arma: {self.__arma if self.__arma else 'Ninguna'}"  

    # consultas  
    def estaVivo(self) -> bool:  
        """Devuelve True si el personaje está vivo."""  
        return self.__vida > 0  

    def establecerVida(self, vida: int):  
        """Establece la vida del personaje."""  
        if isinstance(vida, int) and self.MIN_VIDA <= vida <= self.MAX_VIDA:  
            self.__vida = vida  
        else:  
            raise ValueError("El valor de vida debe ser un número entero entre 8 y 100.")  

    def establecerAtaque(self, ataque: int):  
        """Establece el ataque del personaje."""  
        if isinstance(ataque, int) and self.MIN_ATAQUE <= ataque <= self.MAX_ATAQUE:  
            self.__ataque = ataque  
        else:  
            raise ValueError("El valor de ataque debe ser un número entero entre 5 y 50.")  

    def establecerDefensa(self, defensa: int):  
        """Establece la defensa del personaje."""  
        if isinstance(defensa, int) and defensa >= self.MIN_DEFENSA:  
            self.__defensa = defensa  
        else:  
            raise ValueError("El valor de defensa debe ser un número entero no negativo.")  

    def establecerArma(self, arma: 'Arma'):  
        """Establece el arma del personaje."""  
        if isinstance(arma, Arma):  
            self.__arma = arma  
        else:  
            raise ValueError("El arma debe ser un objeto de la clase Arma.")  
        
    def atacar(self, otro_personaje:'Personaje'):
        """
        Ataca a otro personaje.
        Requiere que otro_personaje esté ligado a un objeto Personaje (no sea None), sino retorna ValueError.
        """    
        
        if isinstance(otro_personaje, Personaje):
            if self.estaVivo():
                if self.__arma!=None:
                    # Si el personaje tiene un arma, se suma el daño del arma al ataque
                    otro_personaje.recibirAtaque(self.__ataque+self.__arma.obtenerDanio())
                else:
                    otro_personaje.recibirAtaque(self.__ataque)
            else:
                otro_personaje.recibirAtaque(self.__ataque)
        else:
            raise ValueError("El personaje a atacar debe ser un objeto de la clase Personaje.")                    

    def recibirAtaque(self, valorAtaque: int):  
        """Recibe un ataque y ajusta la vida del personaje."""  
        if isinstance(valorAtaque, int):  
            if self.estaVivo():  
                daño = max(valorAtaque - self.__defensa, 0)  # Daño mitigado por defensa  
                self.__vida -= daño  
        else:  
            raise ValueError("El valor de ataque debe ser un número entero.")  

    def abrirCaja(self, caja: 'CajaSorpresa'):  
        """Abre una caja sorpresa y ajusta los atributos del personaje."""  
        if isinstance(caja, CajaSorpresa) and self.estaVivo():  
            if caja.obtenerCaracteristica() == Caracteristica.VIDA:
                if self.__vida + caja.obtenerValor() > Personaje.MAX_VIDA:
                    self.__vida = Personaje.MAX_VIDA
                elif self.__vida + caja.obtenerValor() < Personaje.MIN_VIDA:
                    self.__vida = Personaje.MIN_VIDA
                else:
                    self.__vida += caja.obtenerValor()
                    
        elif caja.obtenerCaracteristica() == Caracteristica.ATAQUE:
            if self.__ataque + caja.obtenerValor() > Personaje.MAX_ATAQUE:
                self.__ataque = Personaje.MAX_ATAQUE
            elif self.__ataque + caja.obtenerValor() < Personaje.MIN_ATAQUE:
                self.__ataque = Personaje.MIN_ATAQUE
            else:
                self.__ataque += caja.obtenerValor()                                
    
        elif caja.obtenerCaracteristica() == Caracteristica.DEFENSA:
            if self.__defensa + caja.obtenerValor() > Personaje.MAX_DEFENSA:
                self.__defensa = Personaje.MAX_DEFENSA
            elif self.__defensa + caja.obtenerValor() < Personaje.MIN_DEFENSA:
                self.__defensa = Personaje.MIN_DEFENSA
            else:
                self.__defensa += caja.obtenerValor()
                
                
    def clonar(self) -> 'Personaje':
        """ Devuelve un clon del personaje. """
        clon = Personaje(self.__nombre, self.__ataque, self.__defensa)
        clon.establecerVida(self.__vida)
        if self.__arma:  # Solo clona el arma si no es None
            clon.establecerArma(self.__arma.clonar())  # Aseguramos clonar el arma
        return clon
 
    def esIgual(self, otro: 'Personaje') -> bool:
        """ Devuelve True si el personaje es igual a otro, False en caso contrario. """
        if isinstance(otro, Personaje):
            return (self.__nombre == otro.obtenerNombre() and 
                    self.__vida == otro.obtenerVida() and 
                    self.__ataque == otro.obtenerAtaque() and 
                    self.__defensa == otro.obtenerDefensa() and
                    (self.__arma is None and otro.obtenerArma() is None or
                    self.__arma is not None and self.__arma.esIgual(otro.obtenerArma())))
        else:
            raise ValueError("El personaje a comparar debe ser un objeto de la clase Personaje.")

        
    def copiarValores(self,otro:'Personaje'):
        """Copia los valores de otro personaje. Retorna ValueErro si no recibe un Personaje."""
        if isinstance(otro,Personaje):
            self.__nombre = otro.obtenerNombre()
            self.__vida = otro.obtenerVida()
            self.__ataque = otro.obtenerAtaque()
            self.__defensa = otro.obtenerDefensa()
            self.__arma = otro.obtenerArma()
        else:
            raise ValueError("El personaje a copiar debe ser un objeto de la clase Personaje.")            
    
                           
        