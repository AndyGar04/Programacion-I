from Persona import Persona
from Fecha import Fecha
from datetime import date

class Empleado(Persona):
    def __init__(self, nombre:str = "", direccion:str = "", telefono:str = "", email:str = "", basico:float=5000.0, cantHijos:int=0, fechaIngreso:Fecha = Fecha(1,1,2024)):
        super().__init__(nombre, direccion, telefono, email)
        if not isinstance(basico, (int,float)) or basico < 0:
            raise ValueError("El sueldo basico debe ser un numero positivo")
        if not isinstance(cantHijos, int) or cantHijos < 0:
            raise ValueError("La cantidad de hijos debe ser un numero entero positivo")
        if not isinstance(fechaIngreso, Fecha):
            raise ValueError("La fecha de ingreso debe ser un objeto de tipo fecha")

        self._basico = basico
        self._cantHijos = cantHijos
        self._fechaIngreso = fechaIngreso
        #Atributos privados, no hay subclases que deban accederlos
    
    #Consultas
    def obtenerBasico(self)->float:
        return self._basico
    
    def obtenerCantHijos(self)->int:
        return self._cantHijos
    
    def obtenerFechaIngreso(self)->'Fecha':
        return self._fechaIngreso
    
    def diasVacaciones(self)->int:
        antiguedad = int(self._fechaIngreso.diferenciaHoy())
        vacaciones = 0
        
        if 0 < antiguedad < 5:
            vacaciones = 7
        elif antiguedad < 10:
            vacaciones = 15
        else:
            vacaciones=21
        return vacaciones
    
    """
      -masAntiguo(empleado: Empleado): booleano
        Retorna verdadero si el empleado que recibe el
        mensaje es más antiguo que el argumento
    """
    
    def masAntiguo(self, empleado: 'Empleado') -> bool:
        masAntiguo = False
        
        # Comparar los años de ingreso
        if self._fechaIngreso.obtenerAnio() < empleado.obtenerFechaIngreso().obtenerAnio():
            masAntiguo = True
        elif self._fechaIngreso.obtenerAnio() == empleado.obtenerFechaIngreso().obtenerAnio():
            # Comparar los meses si los años son iguales
            if self._fechaIngreso.obtenerMes() < empleado.obtenerFechaIngreso().obtenerMes():
                masAntiguo = True
            elif self._fechaIngreso.obtenerMes() == empleado.obtenerFechaIngreso().obtenerMes():
                # Comparar los días si los meses también son iguales
                if self._fechaIngreso.obtenerDia() < empleado.obtenerFechaIngreso().obtenerDia():
                    masAntiguo = True
        
        return masAntiguo
    
    """
        sueldoNeto (montoPorHijo: real, fecha: Fecha): real
        Retorna el salario básico más $1000 si tiene entre 10
        y 15 años de antigüedad y $2000 si tiene más de 15
        años de antigüedad. A este valor se le suma un valor
        por cada hijo. 
    """
    
    def sueldoNeto(self, montoPorHijo:float, fecha:Fecha)->float:
        
        plusAntiguedad=0
        
        fecha_actual = date(fecha.obtenerDia(),fecha.obtenerMes(),fecha.obtenerAnio())
        fecha_instancia = date(self.__anio, self.__mes, self.__dia)

        # Calcular la diferencia de años
        diferencia_anios = fecha_actual.year - fecha_instancia.year

        # Ajustar si la fecha actual aún no ha alcanzado el mes y día de la fecha de la instancia
        if (fecha_actual.month, fecha_actual.day) < (self.__mes, self.__dia):
            diferencia_anios -= 1
            
        if diferencia_anios > 10 and diferencia_anios <= 15:
            plusAntiguedad=1000
        elif diferencia_anios > 15:
            plusAntiguedad=2000
            
        sueldo=self._basico+plusAntiguedad+self._cantHijos*montoPorHijo
        
        return sueldo        
                
    
    
    
    

    
            
                
                                     
            
    
        