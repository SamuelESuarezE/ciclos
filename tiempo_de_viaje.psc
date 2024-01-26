Algoritmo tiempo_de_viaje
	flag <- verdadero
	Mientras flag Hacer
		Escribir 'Duracion del tramo:'
		Leer nuevo_viaje
		Si nuevo_viaje==0 Entonces
			flag <- falso
		FinSi
		viajes <- viajes+nuevo_viaje
	FinMientras
	enteroVar <- trunc(viajes/60)
	resto <- viajes MOD 60
	Escribir 'Tiempo total de viaje: ', enteroVar, ':', resto
FinAlgoritmo
