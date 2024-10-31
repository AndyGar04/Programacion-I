from Persona import Persona
from Cliente import Cliente
from Empleado import Empleado
from Fecha import Fecha

class GestionEmpresa:
    @staticmethod
    def gestionar():
        mariaGonzales = Empleado("Maria Gonzalez", "Av. Alem 123", "1234567", "Mail@empresa.com", 30000, 2, Fecha(1,1,2010))
        print(mariaGonzales.obtenerNombre())
        print(mariaGonzales.obtenerDireccion())
        print(mariaGonzales.obtenerBasico())
        
        cliente = Cliente("Juan Perez", "Av. Mitre 123", "1234567", "mail@gmail.com", ciudad="Bahia Blanca", CUIT="20-12345687-9", categoriaIVA="C")
        print(cliente.obtenerNombre())
        print(cliente.obtenerDireccion())
        print(cliente.obtenerSaldo())
        print(cliente.obtenerCiudad())
        
        