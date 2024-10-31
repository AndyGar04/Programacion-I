#3. Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura

Ancho=float(input("Dame el ancho de la habitacion "))
Largo=float(input("Dame el largo de la habitacion "))
Alto=float(input("Dame el alto de la habitacion "))
ManosDePintura=int(input("Dame la cantidad de mando de pintura "))

AreaPorPintar=2 * (Alto*Largo) + 2 * (Alto*Ancho)
AreaPuerta=0.8*2

AreaTotalPorPintar=AreaPorPintar-AreaPuerta

LitrosDePinturaNecesario=(AreaTotalPorPintar/10)*ManosDePintura

print(f"Los litros necesarios son {LitrosDePinturaNecesario}")
