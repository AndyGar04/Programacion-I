# 5. Dado un rango de números, crea una lista que contenga todos los números primos
# dentro de ese rango utilizando list comprehensions.

Limite=int(input("Dame un limite y te dire los primos anteriores"))
PrimosHasta=list()

for i in range(1,Limite,1):
    count=0
    for j in range(1,i,1):
        if (i % j == 0):
            count+=1
        elif(i % 2 == 0 or i % 3 == 0):
            count+=1    
    if (count<=2):
        PrimosHasta.append(i)

PrimosHastaGPT = []

for i in range(1, Limite, 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        PrimosHastaGPT.append(i)
    elif count == 1:
        PrimosHastaGPT.append(i)    

PrimosHastaLim =[1] + [i for i in range(1, Limite,1) if sum(1 for j in range(1, i+1) if i % j == 0) == 2]
print(list(PrimosHasta))
print(list(PrimosHastaGPT))
print(list(PrimosHastaLim))