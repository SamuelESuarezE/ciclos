# Escriba un programa que muestre una tabla de multiplicar como la siguiente:

for num in range(1,11):
    print("\n")
    for x in range(1,11):
        print(str(x*num).rjust(3), end=" ")