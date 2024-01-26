Algoritmo secuencia_de_collatz1
	Escribir 'n:'
	Leer num
	Mientras num<>1 Hacer
		Escribir num, ' 'Sin Saltar
		Si num MOD 2==0 Entonces
			num <- num/2
		SiNo
			num <- (num*3)+1
		FinSi
	FinMientras
	Escribir 1
FinAlgoritmo
