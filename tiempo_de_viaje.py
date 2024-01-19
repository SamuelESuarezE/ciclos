# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como 
# resultado el tiempo total de viaje en formato horas:minutos.
viajes = []

while True:
    nuevo_viaje = int(input("Duracion del tramo: "))
    if nuevo_viaje==0: break
    viajes.append(nuevo_viaje)
entero = int(sum(viajes)/60)
resto = sum(viajes)%60
print(f"Tiempo total de viaje: {entero}:{resto}")