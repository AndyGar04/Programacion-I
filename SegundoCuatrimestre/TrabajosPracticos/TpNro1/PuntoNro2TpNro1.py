# 2. Implemente un programa que a partir del ancho, alto y largo de una habitación
# rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo
# que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una
# puerta de 0,80 de ancho por 2 mts de alto. 

Ancho=float(input("Dame el ancho de la habitacion "))
Largo=float(input("Dame el largo de la habitacion "))
Alto=float(input("Dame el alto de la habitacion "))

AreaPorPintar=2 * (Alto*Largo) + 2 * (Alto*Ancho)
AreaPuerta=0.8*2

AreaTotalPorPintar=AreaPorPintar-AreaPuerta

LitrosDePinturaNecesario=AreaTotalPorPintar/10

print(f"Los litros necesarios son {LitrosDePinturaNecesario}")
