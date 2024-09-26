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