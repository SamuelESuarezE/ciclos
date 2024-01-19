# Escriba un programa que entregue todos los divisores del número entero ingresado:

numero = int(input("Ingresa un numero: "))

for x in range(1, numero+1):
    if numero%x==0: print(x, end=" ")