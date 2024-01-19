# Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

def rectangulo():
    altura = int(input("Altura: "))
    ancho = int(input("Ancho: "))

    for x_altura in range(altura):
        print("\n")
        print("*", end="")
        for x_ancho in range(ancho-1):
            print("*".rjust(4), end="")
    print("\n")
rectangulo()

# Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

def triangulo():
    altura = int(input("Altura: "))
    
    for x_altura in range(altura+1):
        print("*"*x_altura)
triangulo()
# Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

def hexagono():
    lado = int(input("Lado: "))
    
    for fila in range(lado * 2 - 1):
        espacios = abs(lado - 1 - fila)
        print(" " * espacios, end="")
        
        if fila < lado or fila >= lado * 2 - 1:
            print("* " * (lado + fila), end="")
        else:
            print("* ", end="")
        
        print("")
hexagono()