# 14. Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad
# total de vocales que aparecen y lo muestre por pantalla.

Palabra=input("Dame una palabra u frase")
CantVocales=0

for i in range(len(Palabra)):
    if Palabra[i]=="a" or Palabra[i]=="e" or Palabra[i]=="o" or Palabra[i]=="u" or Palabra[i]=="i":
        CantVocales+=1

print(f"La cantidad de vocales es... {CantVocales}")        