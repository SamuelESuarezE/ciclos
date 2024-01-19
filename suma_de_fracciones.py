# Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
denominadores = []
acumulador_list = []
acumulador = 0
decimal = 100000


for x in range(10):
    print(x) 

for num in range(100):
    denominador= 2**num
    decimal = 1/denominador
    denominadores.append(denominador)
    acumulador+=decimal
    acumulador_list.append(acumulador)
    if decimal<=0.000001: break
    
