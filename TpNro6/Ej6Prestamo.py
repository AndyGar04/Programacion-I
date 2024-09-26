    
from Fecha import Fecha
from Ej6Socio import Socio
from Ej6Libro import Libro

class Prestamo():

    #Atributos

    #Contructor
    def __init__ (libro:'Libro',fechaPrestamo:'Fecha', cantDias:int,socio:'Socio'):
        self.__libro=libro
        self.__fechaPrestamo=fechaPrestamo
        self.__cantDias=cantDias
        self.__socio=socio
        self.__fechaDevolucion=None

    #Comando

    """
    ○-> EstablecerFechaDevolucion recibe como parámetro la fecha en la que
    efectivamente se realizó la devolución del libro, y controla si el socio debe
    recibir una penalización, en caso afirmativo se le asigna al socio la fecha de
    penalización.
    """    

    def establecerFechaDevolucion(self,fechaDev:'Fecha'):
        self.__fechaDevolucion=fechaDev

    #Consulta
    def obtenerLibro(self)->'Libro':
        return self.__libro

    def obtenerFechaPrestamo(self)->'Fecha':
        return self.__fechaPrestamo

    """
    ○-> ObtenerFechaDevolución retorna la fecha en la que efectivamente se realizó
    la devolución del libro.
    """    

    def obtenerFechaDevolucion(self)->'Fecha':
        return self.__fechaDevolucion

    """
    ○-> EstaAtrasado recibe como parámetro la fecha actual y retorna verdadero si el
    libro no se devolvió y ya debería haberse devuelto de acuerdo a la fecha de
    préstamo y la cantidad de días.
    """

    def estaAtrasado(self, fechaActual: 'Fecha') -> bool:
        atrasado = True

        if self.__fechaDevolucion is not None:
            if fechaActual.obtenerAnio() > self.__fechaDevolucion.obtenerAnio():
                atrasado = False
            elif fechaActual.obtenerAnio() == self.__fechaDevolucion.obtenerAnio():
                if atrasado.obtenerMes() > self.__fechaDevolucion.obtenerMes():
                    habilitado = False
                elif atrasado.obtenerMes() == self.__fechaDevolucion.obtenerMes():
                    if fechaActual.obtenerDia() > self.__fechaDevolucion.obtenerDia():
                        atrasado = False
                    else:
                        atrasado = True
                else:
                    atrasado = True
            else:
                atrasado = True

        return atrasado 

    """
    ○-> Penalizacion calcula la cantidad de días de penalización y devuelve la fecha
    hasta la que corresponde aplicar la penalización, a partir de la fecha de
    devolución, que tiene que estar ligada. La penalización es de 3 días si se
    atrasó menos de una semana, 5 días si se atrasó menos de tres semanas y
    10 días si se atrasó 3 semanas o más. Si el libro tiene categoría A los días de
    penalización se duplican.
    """

    def Penalizacion(self)->int:
           