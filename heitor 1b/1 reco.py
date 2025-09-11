positivos = 0
negativos = 0
soma =0
valor_1=positivos + negativos
while positivos + negativos <19:
	valor = int(input("Digite um valor inteiro: "))
	if valor > 0:
		positivos += 1
		soma+= valor
	elif valor < 0:
		negativos += 1
print("Soma dos números positivos:", soma)
print("Quantidade de valores negativos:", negativos)