"""
b. implementar una clase tester que verifique los servicios de la clase Vinoteca
con valores significativos.

"""

from EjercicioNro3Tp4 import Vinoteca

class TestEjercicio3Tp4:
    @staticmethod
    
    def test():
        Vinoteca_1=Vinoteca()
        Cantidad=int(input("Dame una cantidad")) 
        Vinoteca_1.venderJugos(Cantidad)   
        Vinoteca_1.venderVinosBlancos(Cantidad)   
        Vinoteca_1.venderVinosTintosAnejado(Cantidad)   
        Vinoteca_1.venderVinosTintosJoven(Cantidad) 

        Vinoteca_1.ObtenerCantidadJugos()
        Vinoteca_1.ObtenerCantidadVinosBlancos()
        Vinoteca_1.ObtenerCantidadVinosTintoAnejado()
        Vinoteca_1.ObtenerCantidadVinosTintoJovenes()  

        Vinoteca_1.reponerJugos()
        Vinoteca_1.reponerVinosBlancos()
        Vinoteca_1.reponerVinosTintosAnejado()
        Vinoteca_1.reponerVinosTintosJoven()

        Vinoteca_1.venderJugos(7)   
        Vinoteca_1.venderVinosBlancos(2700)   
        Vinoteca_1.venderVinosTintosAnejado(5000)   
        Vinoteca_1.venderVinosTintosJoven(5001)

        Vinoteca_1.ObtenerCantidadJugos()
        Vinoteca_1.ObtenerCantidadVinosBlancos()
        Vinoteca_1.ObtenerCantidadVinosTintoAnejado()
        Vinoteca_1.ObtenerCantidadVinosTintoJovenes()
        
if __name__ == "__main__":
    TestEjercicio3Tp4.test()