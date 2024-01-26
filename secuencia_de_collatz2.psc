Algoritmo secuencia_de_collatz2
	definir asterisco Como Entero
	Escribir "n:"
	leer num
	para x<-1 hasta num Hacer
		numero_actual<-x
		veces<-1
		mientras numero_actual<>1 Hacer
			si numero_actual MOD 2 ==0 Entonces
				numero_actual<-numero_actual/2
			SiNo
				numero_actual<-(numero_actual*3)+1
			FinSi
			veces<- veces+1
		FinMientras
		escribir x," ",veces*convertirANumero("0")
	FinPara
	
FinAlgoritmo
