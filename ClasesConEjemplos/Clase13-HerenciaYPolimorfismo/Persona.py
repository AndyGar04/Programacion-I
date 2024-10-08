

class Persona:
    def __init__(self, nombre:str = "", direccion:str = "", telefono:str = "", email:str = ""):
        if not isinstance(nombre,str) or nombre.isspace():
            raise ValueError("El nombre debe ser un string valido")
        if not isinstance(direccion,str) or direccion.isspace():
            raise ValueError("La direccion debe ser un string valido")
        if not isinstance(telefono,str) or telefono.isspace():
            raise ValueError("El telefono debe ser un string valido")
        if not isinstance(email, str) or email.isspace():
            raise ValueError("El email debe ser un string valido")
        
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
        #Estos atributos estan protegidos (no privados)
        
    def obtenerNombre(self)->str:
        return self._nombre
    
    def obtenerDireccion(self)->str:
        return self._direccion
    
    def obtenerTelefono(self)->str:
        return self._telefono
    
    def obtenerEmail(self)->str:
        return self._email    