# Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:

n = int(input("n: "))
denominadores = []
for deno in range(1, n):
    if deno%2!=0:
        denominadores.append(deno)
