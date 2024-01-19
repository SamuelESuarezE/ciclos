# Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

def rectangulo():
    altura = int(input("Altura: "))
    ancho = int(input("Ancho: "))

    for x_altura in range(altura):
        print("", end="\n")
        print("* ", end="")
        for x_ancho in range(ancho-1):
            print("* ", end="")
    print("\n")

# Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

def triangulo():
    altura = int(input("Altura: "))
    
    for x_altura in range(altura+1):
        print("*"*x_altura)

# Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

def hexagono():
    lado = int(input("Lado: "))
    
    # Altura
    for x in range((lado)-1):
        print("*"*(lado+x))
hexagono()