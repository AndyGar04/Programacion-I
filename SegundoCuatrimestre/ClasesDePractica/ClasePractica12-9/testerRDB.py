from claseRobotDeBatalla import RobotDeBatalla
import random 
class TesterRobotDeBatalla:
    @staticmethod
    def test():
        robot1 = RobotDeBatalla("Terminator")
        robot2 = RobotDeBatalla("Optimus Prime")
        print(robot1)
        print(robot2)
        print("*"*70)
        print("Empiezan los ataques")
        print("*"*70)
        while robot1.estaVivo() and robot2.estaVivo():
            atacante = random.randint(1,2000)
            if atacante % 2 == 0:
                print(f"{robot1.obtenerNombre()} ATACA")
                robot1.atacar(robot2)
            else:
                print(f"{robot2.obtenerNombre()} ATACA")
                robot2.atacar(robot1)
            print(robot1)
            print(robot2)
            print("*"*70)
        
        if robot1.estaVivo():
            print(f"{robot1.obtenerNombre()} es el GANADOR")
        else:
            print(f"{robot2.obtenerNombre()} es el GANADOR")


if __name__ == "__main__":
    TesterRobotDeBatalla.test()
