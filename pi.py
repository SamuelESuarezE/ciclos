# Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:

n = int(input("n: "))
aprox = []

for x in range(n):
    estimado = ((-1)**x)/((2*x)+1)
    aprox.append(estimado)
suma = sum(aprox)*4
print(suma)

    
