positivos = 0
negativos = 0
for i in range(20):
	valor = int(input("Digite um valor inteiro: "))
	if valor > 0:
		positivos += valor
	elif valor < 0:
		negativos += 1
print("Soma dos números positivos:", positivos)
print("Quantidade de valores negativos:", negativos)

