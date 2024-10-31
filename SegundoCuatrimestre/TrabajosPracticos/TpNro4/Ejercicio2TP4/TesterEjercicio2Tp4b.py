"""
b. Escribir una clase tester para verificar los servicios de la clase Empleado
utilizando el constructor con todos los parámetros. Esta verificación debe
permitir al usuario ingresar los datos de un empleado (legajo, cantidad de
horas trabajadas en el mes, y valor de la hora) y luego mostrar su legajo y el
sueldo calculado
"""

from EjercicioNro2Tp4 import Empleado

class TestEjercicio2Tp4b:
    @staticmethod
    
    def test():
        legajo=int(input("Dame un legajo"))
        cantHoras=int(input("Dame la cantidad de horas trabajadas"))
        valorHoras=float(input("Dame el valor de cada hora"))
        empleado_1=Empleado(legajo,cantHoras,valorHoras)

        print(f"Su legajo es {empleado_1.obtenerLegajo()}, y su sueldo es {empleado_1.obtenerSueldo()}$")

if __name__ == "__main__":
    TestEjercicio2Tp4b.test()