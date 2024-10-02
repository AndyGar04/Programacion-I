from Arma import Arma
from Personaje import Personaje
from CajaSorpresa import CajaSorpresa

class TesterValoresCopias:  
    
    @staticmethod  
    
    def test():  
        personaje1 = Personaje("El Mago Loco", 25, 20)  
        personaje2 = Personaje("La Princesa Valiente", 30, 22)  
        personaje3 = Personaje("El Guerrero Cobarde", 25, 15)  
        arma1 = Arma("Espada", "Corte cuerpo a cuerpo", 10)  
        arma2 = Arma("Arco", "Ataque a distancia", 8)  
        arma3 = Arma("Bastón", "Cuerpo a cuerpo", 5)  
        personaje2.establecerArma(arma2)  
        personaje3.establecerArma(arma3)  

        arma4 = arma1.clonar()  
        arma5 = arma2.clonar()  
        personaje4 = personaje1.clonar()  
        personaje5 = personaje2.clonar()  
        personaje5.establecerArma(arma4)  
        personaje5.establecerArma(arma5)  

        print("personaje1 ->", personaje1)  
        print("personaje4 ->", personaje4)  
        if personaje1.esIgual(personaje4):  
            print("Los personajes 1 y 4 son iguales.")  
        else:  
            print("Los personajes 1 y 4 son distintos.")  

        print("personaje2 ->", personaje2)  
        print("personaje5 ->", personaje5)  
        if personaje2.esIgual(personaje5):  
            print("Los personajes 2 y 5 son iguales.")  
        else:  
            print("Los personajes 2 y 5 son distintos.")
            
            
        
if __name__ == "__main__":
    TesterValoresCopias.test()             