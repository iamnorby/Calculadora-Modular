def ing_numeros():
	print("BIENVENIDOS A LA CALCULADORA MODULAR")
	a=int(input("Ingrese un numero: "))
	b=int(input("Ingrese otro numero: "))
	n=int(input("Ingrese el modulo n: "))
	while a<0 or b<0 or n<0:
		print ("Error, los numeros deben ser positivos")
		a=int(input("Ingrese un numero: "))
		b=int(input("Ingrese otro numero: "))
		n=int(input("Ingrese el modulo n: "))
	return a,b,n

def adicion_mod(a,b,n):
	sumad=(a+b)
	admod=sumad % n
	return admod

def sustraccion_mod(a,b,n):
	restad=(a-b)
	if restad>0:
		sustmod=restad % n
		return sustmod
	else:
		X=(a+n)-b
		aux=b+X
		sustmod=aux % n
		print(f"El numero da negativo, pero si usamos la ecuacion a=b+x mod Zn, \n\
por ende la aplicamos en {a}= {b}+X , con modulo {n} \n\
X da como resultado {X}")
		return sustmod

def mul_mod(a,b,n):
	mulad=(a*b)
	multmod=mulad % n
	return multmod

def reciproco(a,n):
	for b in range(n):
		if mul_mod(a,b,n) == 1:
			inv=b
			return inv
	else:
		return 0

def div_mod(a,b,n):
	if mul_mod(a,reciproco(b,n),n) > 0:
		return mul_mod(a,reciproco(b,n),n)
	else:
		print("Es indeterminado")

def menu(a,b,n):
	while True:
		print ("----------------------------------------------------------------------------------------------------------------------")
		print (f"Que tipo de operacion de arirmetica modular desea realizar con numeros {a} y {b} con modulo {n} \n\
1 para adicion modular\n\
2 para sustraccion modular\n\
3 para multiplicacion modular\n\
4 para division modular\n\
5 para volver a escoger numeros\n\
0 para salir del programa\n\
----------------------------------------------------------------------------------------------------------------------")
		opcion=input("Opción: ")
		if opcion == "1":
			print(f"El resultado de la adicion modular entre {a} y {b} con modulo {n} es igual a: {adicion_mod(a,b,n)}")
		elif opcion == "2":
			print(f"El resultado de la sustraccción modular de {a} y {b} con modulo {n} es igual a: {sustraccion_mod(a,b,n)}")
		elif opcion == "3":
			print(f"El resultado de la multiplicacion modular de {a} y {b} con modulo {n} es igual a: {mul_mod(a,b,n)}")
		elif opcion == "4":
			if reciproco(b,n)==0:
				print ("Es indeterminado")
			else:
				print (f"El reciproco es {reciproco(b,n)}")
				print(f"El resultado de la division modular de {a} y {b} con modulo {n} es igual a: {div_mod(a,b,n)}")
		elif opcion == "5":
			a,b,n=ing_numeros()
			menu(a,b,n)
		elif opcion == "0":
			print("Adios")
			break
		else:
			print("Error 404 Opcion no encontrada, digite nuevamente")
			print ("----------------------------------------------------------------------------------------------------------------------")

a,b,n=ing_numeros()
menu(a,b,n)