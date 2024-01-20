# Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
potencia=1
division=1
acumulador=0
print("Potencia | Fraccion |   Suma")
print("         |          |        ")

while division>0.000001:
    division=1/2**potencia
    acumulador+=division
    print(f"{str(potencia).center(8)} | {str(round(division, 6)).center(8)} | {str(round(acumulador, 6)).center(8)}")
    potencia+=1
