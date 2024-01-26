Algoritmo aproximarPi
	Definir n, aprox como real
	Escribir "n:"
	Leer n
	para x<-0 hasta n Hacer
		estimado<-((-1)^x)/((2*x)+1)
		aprox<- aprox+estimado
	FinPara
	escribir aprox*4
FinAlgoritmo
