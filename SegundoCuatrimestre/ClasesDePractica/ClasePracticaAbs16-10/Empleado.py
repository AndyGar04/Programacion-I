from abc import ABC, abstractmethod
from datetime import datetime

class Empleado(ABC):
    def __init__(self, dni:str, nombre:str, apellido:str, anioIngreso:int):
        if not isinstance(dni, str) or dni =="" or dni.isspace():
            raise TypeError
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise TypeError
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise TypeError
        if not isinstance(anioIngreso, int) or anioIngreso < 0:
            raise TypeError
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._anioIngreso = anioIngreso

    @abstractmethod
    def obtenerSalario(self):
        pass

    def nombreCompleto(self):
        return self._apellido + " " + self._nombre
    
    def antiguedadEnAnios(self):
        return datetime.today().year - self._anioIngreso
    
    def __str__(self):
        return f"{self._dni} - {self._apellido}, {self._nombre} (ingreso: {self._anioIngreso})"
    
class EmpleadoSalarioFijo(Empleado):
    __PORC_2_a_5 = 0.05
    __PORC_MAS_DE_5 = 0.1
    __ANiO_LIMITE_INFERIOR = 2
    __ANiO_LIMITE_SUPERIOR = 5

    def __init__(self, dni:str, nombre:str, apellido:str, anioIngreso:int, sueldoBasico: float):
        super().__init__(dni, nombre, apellido, anioIngreso)
        if not isinstance(sueldoBasico, (int, float)) or sueldoBasico <= 0:
            raise ValueError
        self.__sueldoBasico = sueldoBasico

    def obtenerPorcentajeAdicional(self):
        porcentaje = 0
        if self.antiguedadEnAnios() > EmpleadoSalarioFijo.__ANiO_LIMITE_SUPERIOR:
            porcentaje = EmpleadoSalarioFijo.__PORC_MAS_DE_5
        elif self.antiguedadEnAnios() >= EmpleadoSalarioFijo.__ANiO_LIMITE_INFERIOR:
            porcentaje = EmpleadoSalarioFijo.__PORC_2_a_5
        return porcentaje

    def obtenerSalario(self)-> float:
        return self.__sueldoBasico + self.__sueldoBasico * self.obtenerPorcentajeAdicional()

    def __str__(self):
        return f"{super().__str__()} - Salario: $ {self.obtenerSalario()}"

class EmpleadoAComision(Empleado):
    def __init__(self, dni:str, nombre:str, apellido:str, anioIngreso:int, salarioMinimo: float, cantClientesCaptados: int, montoPorCliente: float):
        super().__init__(dni, nombre, apellido, anioIngreso)
        if not isinstance(salarioMinimo, (int, float)) or salarioMinimo<=0:
            raise ValueError
        if not isinstance(cantClientesCaptados, int) or cantClientesCaptados<0:
            raise ValueError
        if not isinstance(montoPorCliente, (int, float)) or montoPorCliente<0:
            raise ValueError
        self.__salarioMinimo=salarioMinimo
        self.__cantClientesCaptados = cantClientesCaptados
        self.__montoPorCliente=montoPorCliente

    def obtenerSalario(self)->float:
        salario = self.__cantClientesCaptados * self.__montoPorCliente
        if salario < self.__salarioMinimo:
            salario = self.__salarioMinimo
        return salario
    
    def obtenerCantClientesCaptados(self):
        return self.__cantClientesCaptados
    
    def __str__(self):
        return f"{super().__str__()} - Cantidad de clientes captados: {self.__cantClientesCaptados} - Salario: ${self.obtenerSalario}"
    
class Empresa():
    def __init__(self):
        self.__listaEmpleados = []

    def agregarEmpleado(self, empleado:'Empleado'):
        if not isinstance(empleado, Empleado):
            raise ValueError("La empleado debe ser de tipo Empleado")
        else:
            if empleado not in self.__empleados:
                self.__empleados.append(empleado)
            else:
                print(f"La empleado {empleado.obtenerNombre()} ya está asignada a esta empresa.")

    def eliminarEmpleado(self, empleado:'Empleado'):
        if not isinstance(empleado, Empleado):
            raise ValueError("El empleado debe ser de tipo Empleado")
        
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
            print(f"La empleado {empleado.obtenerNombre()} fue eliminado.")
        else:
            print("La empleado no existe en la empresa.")
            
    def masClientesCaptados(self)->'EmpleadoAComision':
        """Devuelve el empleado a comisión con más clientes captados usando obtenerClientesCaptados."""
        empleados_comision = [emp for emp in self.empleados if isinstance(emp, EmpleadoAComision)]
        
        if not empleados_comision:
            return None  # No hay empleados a comisión
        
        # Inicializar con None y hacer la comparación desde el inicio
        empleado_max_clientes = None
        max_clientes = -1  # Inicializamos con un valor menor a cualquier número de clientes
        
        # Recorrer todos los empleados a comisión
        for empleado in empleados_comision:
            if empleado.obtenerClientesCaptados() > max_clientes:
                max_clientes = empleado.obtenerClientesCaptados()
                empleado_max_clientes = empleado
        
        return empleado_max_clientes
    
    
              