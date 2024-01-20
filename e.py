# Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
import math
lista = []
x = 0
e_anterior=0
diferencia=1
e=0
numero_anterior=0
numero=2

while diferencia>0.0001 or diferencia==0:
    e_anterior = e
    numero_anterior=numero
    e = 1/math.factorial(x)
    lista.append(e)
    x+=1
    numero = sum(lista) - e_anterior
    diferencia = abs(numero-numero_anterior)
    
print(numero)
    
