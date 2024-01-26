Algoritmo suma_entre_numeros
	Definir num1, num2, suma Como Entero
	Escribir 'Ingrese primer numero:'
	Leer num1
	Escribir 'Ingrese segundo numero:'
	Leer num2
	Para x<-num1+1 Hasta num2-1 Hacer
		suma <- suma+x
	FinPara
	Escribir suma
FinAlgoritmo
