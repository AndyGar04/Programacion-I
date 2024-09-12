"""
c. Escribir otra clase tester para verificar los servicios de la clase Empleado.
Esta verificación debe permitir al usuario ingresar los datos de un empleado
(legajo, cantidad de horas trabajadas en el mes, y valor de la hora), crear el
objeto empleado utilizando el constructor con el parámetro legajo, y luego
modificar los demás atributos del objeto con los servicios provistos por la
clase. Finalmente debe mostrar por pantalla el legajo y el sueldo del
empleado.
"""

from EjercicioNro2Tp4 import Empleado

class TestEjercicio2Tp4c:
    @staticmethod
    
    def test():
        legajo=int(input("Dame un legajo"))
        empleado_1=Empleado(legajo)

        print(f"Su legajo es {empleado_1.obtenerLegajo()}, trabaja {empleado_1.obtenerHorasTrabajadas()} horas al mes y {empleado_1.obtenerValorHora()} valor hora")

        empleado_1.establecerHorasTrabajadas(int(input("Dame las horas que trabajó: ")))
        empleado_1.establecerValorHora(float(input("Dame el valor de las horas: ")))

        print(f"Horas trabajadas: {empleado_1.obtenerHorasTrabajadas()}")
        print(f"Valor por hora: {empleado_1.obtenerValorHora()}")

        print(f"Su legajo es {empleado_1.obtenerLegajo()}, y su sueldo es {empleado_1.obtenerSueldo()}$")
        
if __name__ == "__main__":
    TestEjercicio2Tp4c.test()