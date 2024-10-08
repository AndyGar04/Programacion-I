from classAuto import Auto
from classCamion import Camion
from classColectivo import Colectivo
from classMoto import Moto
from classTicket import Ticket
import random

class SimulacionPeaje:
    @staticmethod
    def simular():
        lista_tickets = []
        cantIteraciones = int( input("Cuantos vehículos quiere testear?:"))
        for i in range(cantIteraciones):
            opcion = random.randint(1,4)
            if opcion == 1:
                veh = Camion("camionPAT", random.randint(2,5), random.randint(100,15000))
            elif opcion ==2:
                veh = Colectivo("colePat", random.randint(0,50)   )
            elif opcion==3:
                veh = Auto("autoPAt", random.randint(1, 5))
            else:
                veh = Moto("motoPat")
            ticket = Ticket(veh)
            lista_tickets.append(ticket)
        
        print(f"Se generaron {len(lista_tickets)} tickets")
        for tic in lista_tickets:
            print(tic)

if __name__ == "__main__":
    SimulacionPeaje.simular()