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

    def obtieneNombre(self) -> str:
        """Devuelve el nombre del personaje."""
        return self.__nombre

    def obtieneVida(self) -> int:
        """Devuelve la vida del personaje."""
        return self.__vida

    def obtieneAtaque(self) -> int:
        """Devuelve el ataque del personaje."""
        return self.__ataque

    def obtieneDefensa(self) -> int:
        """Devuelve la defensa del personaje."""
        return self.__defensa

    def obtenerArma(self):
        """Devuelve el arma del personaje."""
        return self._arma

    def __str__(self):
        """Devuelve una representación de string del personaje."""
        return f"Nombre: {self._nombre}, Vida: {self._vida}, Ataque: {self._ataque}, Defensa: {self._defensa}, Arma: {self._arma if self._arma else 'Ninguna'}"

    #consultas
    def estaVivo(self):
        """Devuelve True si el personaje está vivo."""
        return self.__vida > 0

    def establecerVida(self, vida:int):
        """Establece la vida del personaje. Retorna ValueError si no recibe un número entero."""
        if isinstance(vida, int) and VIDA_MIN <= vida <= VIDA_MAX:
            self.__vida = vida
        else:
            raise ValueError("El valor de vida debe ser un número entero.")

    def establecerAtaque(self,ataque:int):        
        """Establece el ataque del personaje. Retorna ValueError si no recibe un número entero positivo."""
        if isinstance(ataque, int) and ATAQUE_MIN <= ataque <= ATAQUE_MAX:
            self.__ataque = ataque
        else:
            raise ValueError("El valor de ataque debe ser un número entero positivo.")

    def establecerDefensa(self, defensa: int):
        """Establece la defensa del personaje. Retorna ValueError si no recibe un número entero."""
        if isinstance(defensa, int) and defensa >= Personaje.MIN_DEFENSA:
            self.__defensa = defensa
        else:
            raise ValueError("El valor de defensa debe ser un número entero positivo.")

    def establecerArma(self, arma):
        """Establece el arma del personaje. Retorna ValueError si no recibe un arma."""
        if isinstance(arma, Arma):
            self.__arma = arma
        else:
            raise ValueError("El arma debe ser un objeto de la clase Arma.")

    def establecerDefensa(self, defensa: int):
        """Establece la defensa del personaje. Retorna ValueError si no recibe un número entero."""
        if isinstance(defensa, int) and defensa >= Personaje.MIN_DEFENSA:
            self.__defensa = defensa
        else:
            raise ValueError("El valor de defensa debe ser un número entero positivo.")

    def establecerArma(self, arma):
        """Establece el arma del personaje. Retorna ValueError si no recibe un arma."""
        if isinstance(arma, Arma):
            self.__arma = arma
        else:
            raise ValueError("El arma debe ser un objeto de la clase Arma.")

    def recibirAtaque(self, valorAtaque: int):
        """ Recibe un ataque y ajusta la vida del personaje. Retorna ValueError si no recibe un número entero. """
        if isinstance(valorAtaque, int):
            if Personaje.MIN_ATAQUE <= valorAtaque <= Personaje.MAX_ATAQUE:
                if self.estáVivo():
                    if self.__defensa < valorAtaque:
                        # Si la defensa del personaje es menor al ataque recibido,
                        # se resta la diferencia a la vida del personaje
                        self.__vida -= (valorAtaque - self.__defensa)
        else:
            raise ValueError("El valor de ataque debe ser un número entero positivo.")

    def abrirCaja(self, caja: CajaSorpresa):  
        """Abre una caja sorpresa y ajusta los atributos del personaje."""  
        if isinstance(caja, CajaSorpresa) and self.estáVivo():  
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

    
    
        