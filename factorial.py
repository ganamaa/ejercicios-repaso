def factorial(num):
   if num == 0 or num == 1:
      return 1
   else:
      return num * factorial(num - 1)


try:
	numero = int(input('ingresa el numero: '))
	calculo = factorial(numero)
	print("El factorial de %s es %s" % (numero, calculo))
except:
	print("\nTiene que ser un valor numerico")


