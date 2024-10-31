"""
5. El tamagotchi es un juego donde el objetivo es mantener
con vida a una “mascota virtual” la mayor cantidad de
tiempo posible. Cada mascota virtual se identifica por medio
de su nombre. Pueden realizar diferentes acciones, las que
aumentan o disminuyen su nivel de energía, el cual nunca
puede disminuir por debajo de 0 ni superar el máximo de
100. Mientras duerme no puede hacer ninguna otra acción,
a menos que antes se lo despierte. Ninguna mascota puede
realizar más de tres acciones de desgaste de energía en
forma consecutiva. Al cuarto intento, ignora la orden dada y
directamente se pone a dormir. Cuando se vuelva a despertar, podrá volver a
realizar a lo sumo tres acciones de desgaste.
La mascota tiene tres estados que debes gestionar: Energía, Diversión e Higiene.
Cada estado se representa con un valor numérico que puede variar entre 0 (muy
bajo) y 100 (muy alto). Al crear la mascota, todos los estados se inicializan en su
máximo valor posible. La mascota tiene varias acciones que pueden influir en estos
estados:
a. Comer: aumenta el nivel de energía en 20 puntos.
b. Beber: aumenta el nivel de energía en 10 puntos.
c. Jugar: aumenta la diversión en 40 puntos, pero reduce la energía en 20
puntos y la higiene en 15 puntos.
d. Caminar: aumenta la diversión en 20 puntos, reduce energía en 10 puntos y
la higiene en 8 puntos.
e. Saltar: aumenta la diversión en 10 puntos, reduce energía en 15 puntos y la
higiene en 10 puntos.
f. Dormir: aumenta la energía en 20 puntos, pero reduce la diversión en 10
puntos.
g. Bañar: aumenta la higiene en 40 puntos, pero reduce la diversión en 10
puntos.
Cada estado tiene un límite máximo de 100 y un mínimo de 0, por lo que si al
realizar una acción se supera o se disminuye ese límite, el valor se ajusta al máximo
o mínimo correspondiente.
Si el nivel de energía de la mascota llega a 0, lamentablemente dejará de existir y no
podrá realizar ninguna actividad más.
"""

class Tamagotchi:
    #Atributos de la clase
    MAX_VALOR=100
    MIN_VALOR=0

    #Atributos de la instacia
    def __init__(self,nombre:str,energia:int=MAX_VALOR,diversion:int=MAX_VALOR,higiene:int=MAX_VALOR,dormido:bool=False,cantActividadesDesgaste:int=MAX_VALOR):
        self.__nombre=nombre
        self.__energia=energia
        self.__diversion=diversion
        self.__higiene=higiene
        self.__dormido=dormido
        self.__cantActvidadesDesgaste=cantActividadesDesgaste

    def comer(self):
        if(self.__energia+20>self.MAX_VALOR):
            self.__energia=self.MAX_VALOR
        else:
            self.__energia=self.__energia+20
        return self.__energia

    def beber(self):
        if(self.__energia+10>self.MAX_VALOR):
            self.__energia=self.MAX_VALOR
        else:
            self.__energia=self.__energia+10
        return self.__energia         

    def dormir(self):
        if self.__dormido:
            print("ZZZzzzz...(ya estaba durmiendo)")
        else:    
            if self.__energia + 20 > self.MAX_VALOR:
                self.__energia = self.MAX_VALOR
            else:
                self.__energia += 20
            if self.__diversion - 10 < self.MIN_VALOR:
                self.__diversion = self.MIN_VALOR
            else:
                self.__diversion -= 10   
            print("Durmiendo...")
            self.__dormido = True
        return self.__energia, self.__diversion, self.__dormido                  

    def despertar(self):
        if (self.__dormido==True):
            self.__dormido=False
            print("Me desperte...")
        else:
            print("Ya estoy despierto...") 
        return self.__dormido

    def jugar(self):
        if(self.__diversion+40>self.MAX_VALOR):
            self.__diversion=self.MAX_VALOR
        else:
            self.__diversion=self.__diversion+40
        if(self.__energia-20<self.MIN_VALOR):
            self.__energia=self.MIN_VALOR
        else:
            self.__energia=self.__energia-20
        if(self.__higiene-15<self.MIN_VALOR):
            self.__higiene=self.MIN_VALOR
        else:
            self.__higiene=self.__higiene-15
        return self.__higiene, self.__energia, self.__diversion

    def caminar(self):
        if(self.__diversion+20>self.MAX_VALOR):
            self.__diversion=self.MAX_VALOR
        else:
            self.__diversion=self.__diversion+20
        if(self.__energia-10<self.MIN_VALOR):
            self.__energia=self.MIN_VALOR
        else:
            self.__energia=self.__energia-10
        if(self.__higiene-8<self.MIN_VALOR):
            self.__higiene=self.MIN_VALOR
        else:
            self.__higiene=self.__higiene-8
        return self.__higiene, self.__energia, self.__diversion  

    def saltar(self):
        if(self.__diversion+10>self.MAX_VALOR):
            self.__diversion=self.MAX_VALOR
        else:
            self.__diversion=self.__diversion+10
        if(self.__energia-15<self.MIN_VALOR):
            self.__energia=self.MIN_VALOR
        else:
            self.__energia=self.__energia-15
        if(self.__higiene-10<self.MIN_VALOR):
            self.__higiene=self.MIN_VALOR
        else:
            self.__higiene=self.__higiene-10
        return self.__higiene, self.__energia, self.__diversion 

    def banarse(self): 
        if(self.__diversion-10>self.MIN_VALOR):
            self.__diversion=self.MIN_VALOR
        else:
            self.__diversion=self.__diversion-10
        if(self.__higiene+40>self.MAX_VALOR):
            self.__higiene=self.MAX_VALOR
        else:
            self.__higiene=self.__higiene+40
        return self.__higiene, self.__diversion    

    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerEnergia(self)->int:
        return self.__energia

    def obtenerHigiene(self)->int:
        return self.__higiene

    def estaDormido(self)->bool:
        return self.__dormido

    def estaVivo(self)->bool:
        if (self.__energia==self.MIN_VALOR):
            return False
        else:
            return True     

    def obtenerHumor(self) -> str:
        humor = ""
        if (self.__energia > 70 and self.__diversion > 70 and self.__higiene > 70):
            humor = "Soy un tipo feliz"
        elif (self.__energia > 50 and self.__diversion > 50) or (self.__energia > 50 and self.__higiene > 50) or (self.__diversion > 50 and self.__higiene > 50):   
            humor = "Soy un tipo alegre, la verdad es que podría estar mejor"
        elif (self.__energia > 30 and self.__diversion > 30) or (self.__energia > 30 and self.__higiene > 30) or (self.__diversion > 30 and self.__higiene > 30):
            humor = "En este momento, soy un tipo neutral, creo que la vida me podría tratar mucho mejor"
        elif (self.__energia > 10 and self.__diversion > 10) or (self.__energia > 10 and self.__higiene > 10) or (self.__diversion > 10 and self.__higiene > 10):
            humor = "Algo me dice que no me queda mucho si algo no cambia... Estoy triste"
        else:    
            humor = "La vida no tiene sentido, creo que es momento de abandonarla si algo no cambia *cae en depresión*"    
        return humor    

"""
El humor de la mascota está determinado por la combinación de los valores de
energía, diversión e higiene de la siguiente forma:
● Humor Feliz: Si energía, diversión e higiene están todos por encima de 70.
● Humor Alegre: Si al menos dos de los tres (energía, diversión, higiene) están
entre 50 y 70.
● Humor Neutral: Si al menos dos de los tres están entre 30 y 50.
● Humor Triste: Si al menos dos de los tres están entre 10 y 30.
● Humor Muy Triste: Si al menos dos de los tres están por debajo de 10.
Implementar la clase MascotaVirtual modelada por el siguiente diagrama, pueden
agregarle los métodos que consideren necesarios.
"""