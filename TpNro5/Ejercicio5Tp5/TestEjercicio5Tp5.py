import random
from EjercicioNro5Tp5 import Especies

class TesterEspecie:

    @staticmethod
    def testEspecie():
        # Prueba creación de especies
        print("Prueba creación de especies:")
        especie1 = Especies("Panthera leo")
        especie2 = Especies("Canis lupus", machos=10, hembras=15, ritmo=0.05)
        print(especie1)
        print(especie2)
        print()

        # Prueba actualización de machos, hembras y ritmo
        print("Prueba actualización de machos, hembras y ritmo:")
        especie1.actualizarMachos(5)
        especie1.actualizarHembras(-3)
        especie1.establecerRitmo(0.02)
        print(f"Después de actualizar: {especie1}")
        print()

        # Prueba clonación
        print("Prueba de clonación:")
        clon = especie2.clonar()
        print(f"Especie original: {especie2}")
        print(f"Especie clonada: {clon}")
        print()

        # Prueba de riesgo
        print("Prueba de riesgo de extinción:")
        print(f"{especie1.obtenerNombre()} riesgo: {especie1.riesgo()}")
        print(f"{especie2.obtenerNombre()} riesgo: {especie2.riesgo()}")
        print()

        # Prueba de comparación de ritmos
        print("Prueba de comparación de ritmos:")
        if especie1.mayorRitmo(especie2):
            print(f"{especie1.obtenerNombre()} tiene mayor ritmo que {especie2.obtenerNombre()}")
        else:
            print(f"{especie2.obtenerNombre()} tiene mayor ritmo que {especie1.obtenerNombre()}")
        print()

        # Prueba de población estimada
        print("Prueba de población estimada:")
        anios = 10
        print(f"Población actual de {especie2.obtenerNombre()}: {especie2.poblacionActual()}")
        print(f"Población estimada en {anios} años: {especie2.poblacionEstimada(anios)}")
        print()

        # Prueba de años para alcanzar una población
        print("Prueba de años para alcanzar una población:")
        poblacion_objetivo = 100
        anios_para_poblacion = especie2.aniosParaPoblacion(poblacion_objetivo)
        if anios_para_poblacion == -1:
            print(f"No se alcanzará la población objetivo de {poblacion_objetivo}.")
        else:
            print(f"Se necesitarán {anios_para_poblacion} años para alcanzar una población de {poblacion_objetivo}.")
        print()

if __name__ == "__main__":
    TesterEspecie.testEspecie()