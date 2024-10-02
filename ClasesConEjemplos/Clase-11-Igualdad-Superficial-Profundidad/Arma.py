#from Personaje import Personaje

class Arma:  
    def __init__(self, nombre:str, tipo:str, danio:int):  
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():  
            raise ValueError("El nombre debe ser un string válido.")  
        if not isinstance(tipo, str) or tipo == "" or tipo.isspace():  
            raise ValueError("El tipo debe ser un string válido.")  
        if not isinstance(danio, int) or danio < 0:  
            raise ValueError("El daño debe ser un número entero positivo.")  
        self.__nombre = nombre  
        self.__tipo = tipo  
        self.__danio = danio  

    def obtenerNombre(self):  
        return self.__nombre  

    def obtenerTipo(self):  
        return self.__tipo  

    def obtenerDanio(self):  
        return self.__danio  

    def __str__(self):  
        return f"{self.__nombre}: {self.__tipo} ({self.__danio} de daño)"
    
    def clonar(self) -> 'Arma':  
        """Devuelve un clon de nuestra Arma."""  
        # Verificar que el nombre y tipo son cadenas, danio es un entero positivo  
        if not isinstance(self.__nombre, str) or not isinstance(self.__tipo, str):  
            raise ValueError("El nombre y tipo deben ser cadenas de texto.")  
        if not isinstance(self.__danio, (int, float)) or self.__danio < 0:  
            raise ValueError("El daño debe ser un número entero o de punto flotante no negativo.")  
        
        clon = Arma(self.__nombre, self.__tipo, self.__danio)  
        
        return clon
    
    def esIgual(self, otro:'Arma')->bool:
        """ Devuelve True si el arma es igual a otro, False en caso contrario. Retorna ValueError si no recibe
        un Arma."""
        if isinstance(otro, Arma):
            return (self.__nombre == otro.obtenerNombre() and self.__tipo == otro.obtenerTipo() and self.__danio == otro.obtenerDanio())
        else:
            raise ValueError("El arma a comparar debe ser un objeto de la clase Arma.")
        
    def copiarValores(self,otro:'Arma'):
        """Copia los valores de otro arma. Retorna ValueErro si no recibe un Arma."""
        if isinstance(otro,Arma):
            self.__nombre = otro.obtenerNombre()
            self.__tipo = otro.obtenerTipo()
            self.__danio = otro.obtenerDanio()
        else:
            raise ValueError("El arma a copiar debe ser un objeto de la clase Arma.")  