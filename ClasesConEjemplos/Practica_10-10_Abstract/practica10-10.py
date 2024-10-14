from abc import ABC, abstractmethod
from Fecha import Fecha

class Producto(ABC):
    def __init__(self, id:int, precio:float):
        if not isinstance(id, int):
            raise ValueError("El id debe ser un entero")
        if not isinstance(precio, float):
            raise ValueError("El precio debe ser un flotante")
        self.__id = id
        self.__precio = precio

    def obtener_id(self):
        return self.__id
    
    def obtener_precio(self):
        return self.__precio
    
    @abstractmethod
    def vender(self):
        pass

    @abstractmethod
    def sePuedeVender(self, cantidad:int):
        pass
        
class Consola(Producto):
    def __init__(self, id:int, precio:float, marca:str, modelo:str, almacenamiento:float, cantidadJoysticks:int, stock:int):
        super().__init__(id, precio)
        if not isinstance(marca, str):
            raise ValueError("La marca debe ser una cadena")
        if not isinstance(modelo, str):
            raise ValueError("El modelo debe ser una cadena")
        if not isinstance(almacenamiento, float):
            raise ValueError("El almacenamiento debe ser un flotante")
        if not isinstance(cantidadJoysticks, int):
            raise ValueError("La cantidad de joysticks debe ser un entero")
        if not isinstance(stock, int) or stock <= 0:
            raise ValueError("El stock debe ser un entero positivo")
        self.__marca = marca
        self.__modelo = modelo
        self.__almacenamiento = almacenamiento
        self.__cantidadJoysticks = cantidadJoysticks
        self.__stock = stock
        self.__listaJuegosCompatibles=[]

    def obtener_marca(self):
        return self.__marca
    
    def obtener_modelo(self):
        return self.__modelo
    
    def obtener_almacenamiento(self):
        return self.__almacenamiento
    
    def obtener_cantidadJoysticks(self):
        return self.__cantidadJoysticks
    
    def obtener_stock(self):
        return self.__stock
    
    def establecer_stock(self, stock:int):
        if not isinstance(stock, int) or stock <= 0:
            raise ValueError("El stock debe ser un entero positivo")
        self.__stock = stock

    def agregarStock(self, cantidad:int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
        self.__stock += cantidad

    def obtener_listaJuegosCompatibles(self):
        return self.__listaJuegosCompatibles
    
    def agregarJuegoCompatible(self, juego:"Juego"):
        if not isinstance(juego, Juego):
            raise ValueError("El juego debe ser objeto de la clase Juego")
        self.__listaJuegosCompatibles.append(juego)

    def quitarJuegoCompatible(self, juego:"Juego"):
        if not isinstance(juego, Juego):
            raise ValueError("El juego debe ser objeto de la clase Juego")
        self.__listaJuegosCompatibles.remove(juego)

    def sePuedeVender(self, cantidad:int):
        return self.__stock >= cantidad
    
    def vender(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
        if not self.sePuedeVender(cantidad):
            raise ValueError("No hay suficiente stock")
        self.__stock -= cantidad

class Juego(Producto):
    def __init__(self, id:int, precio:float, nombre: str, genero:str, anio: int, descripcion:str, multijugador:bool):
        super().__init__(id, precio)
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser una cadena")
        if not isinstance(genero, str):
            raise ValueError("El genero debe ser una cadena")
        if not isinstance(anio, int):
            raise ValueError("El anio debe ser un entero")
        if not isinstance(descripcion, str):
            raise ValueError("La descripcion debe ser una cadena")
        if not isinstance(multijugador, bool):
            raise ValueError("El multijugador debe ser un booleano")
        self.__nombre = nombre
        self.__genero = genero
        self.__anio = anio
        self.__descripcion = descripcion
        self.__multijugador = multijugador
        self.__listaConsolasCompatibles = []

    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_genero(self):
        return self.__genero
    
    def obtener_anio(self):
        return self.__anio
    
    def obtener_descripcion(self):
        return self.__descripcion
    
    def obtener_multijugador(self):
        return self.__multijugador
    
    def obtener_listaConsolasCompatibles(self):
        return self.__listaConsolasCompatibles

class JuegoFisico(Juego):
    def __init__(self, id:int, precio:float, nombre: str, genero:str, anio: int, descripcion:str, multijugador:bool, stock:int):
        super().__init__(id, precio, nombre, genero, anio, descripcion, multijugador)
        if not isinstance(stock, int) or stock <= 0:
            raise ValueError("El stock debe ser un entero positivo")
        self.__stock = stock

    def obtener_stock(self):
        return self.__stock
    
    def establecer_stock(self, stock:int):
        if not isinstance(stock, int) or stock <= 0:
            raise ValueError("El stock debe ser un entero positivo")
        self.__stock = stock

    def agregarStock(self, cantidad:int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
        self.__stock += cantidad

    def sePuedeVender(self, cantidad:int):
        return self.__stock >= cantidad

    def vender(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
        if not self.sePuedeVender(cantidad):
            raise ValueError("No hay suficiente stock")
        self.__stock -= cantidad

class JuegoDigital(Juego):
    def __init__(self, id:int, precio:float, nombre: str, genero:str, anio: int, descripcion:str, multijugador:bool, plataforma:str, tamanio:float, distribuidora:str):
        super().__init__(id, precio, nombre, genero, anio, descripcion, multijugador)
        if not isinstance(plataforma, str):
            raise ValueError("La plataforma debe ser una cadena")
        if not isinstance(tamanio, float):
            raise ValueError("El tamanio debe ser un flotante")
        if not isinstance(distribuidora, str):
            raise ValueError("La distribuidora debe ser una cadena")
        self.__plataforma = plataforma
        self.__tamanio = tamanio
        self.__distribuidora = distribuidora

    def obtener_plataforma(self):
        return self.__plataforma
    
    def obtener_tamanio(self):
        return self.__tamanio
    
    def obtener_distribuidora(self):
        return self.__distribuidora
    
    def sePuedeVender(self, cantidad:int):
        return True
        
    def vender(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
        

class Cliente:
    def __init__(self, nombre:str, apellido:str, dni:int, mail:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena")
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser una cadena")
        if not isinstance(dni, int):
            raise ValueError("El dni debe ser un entero")
        if not isinstance(mail, str):
            raise ValueError("El mail debe ser una cadena")
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__mail = mail

class Item:
    def __init__(self, producto:Producto, cantidad:int):
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser un objeto de la clase Producto")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
        self.__producto = producto
        self.__cantidad = cantidad

    def obtener_producto(self):
        return self.__producto
    
    def obtener_cantidad(self):
        return self.__cantidad

class Compra:
    def __init__(self, cliente:Cliente, fecha: Fecha, formaPago:str):
        if not isinstance(fecha, Fecha):
            raise ValueError("La fecha debe ser un objeto de la clase Fecha")
        if not isinstance(formaPago, str):
            raise ValueError("La forma de pago debe ser una cadena")
        if not isinstance(cliente, Cliente):
            raise ValueError("El cliente debe ser un objeto de la clase Cliente")
        self.__fecha = fecha
        self.__formaPago = formaPago
        self.__estado = "Pendiente"
        self.__listaItems = []
        self.__cliente = cliente

    def obtener_fecha(self):
        return self.__fecha
    
    def obtener_formaPago(self):
        return self.__formaPago
    
    def obtener_estado(self):
        return self.__estado
    
    def obtener_cliente(self):
        return self.__cliente
    
    def obtener_listaItems(self):
        return self.__listaItems
    
    def agregarItem(self, item:"Item"):
        if not isinstance(item, Item):
            raise ValueError("El item debe ser un objeto de la clase Item")
        self.__listaItems.append(item)

    def entregar(self):
        self.__estado = "Entregado"
        
    def costoTotal(self):
        total = 0
        for item in self.__listaItems:
            total += item.obtener_producto().obtener_precio() * item.obtener_cantidad()
        return total


