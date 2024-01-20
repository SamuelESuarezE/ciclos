# Desarrolle un programa que entregue la secuencia de Collatz de un número entero

def entero():
    num = int(input("n: "))

    while num!=1:
        print(num, end=" ")
        if num%2==0:
            num=int(num/2)
        else: num=(num*3)+1 
    print(1)
entero()
# Desarrolle un programa que grafique los largos de las secuencias de Collatz de los números enteros positivos menores que el ingresado por el usuario

def grafico():
    num = int(input("n: "))
    
    for x in range(1, num+1):
        numero_actual = x
        veces=1
        while numero_actual!=1:
            if numero_actual%2==0:
                numero_actual=int(numero_actual/2)
            else:
                numero_actual=(numero_actual*3)+1
            veces+=1
        print(f"{x} {veces*'*'}")
        
grafico()