N = int(float(input("Digite um número: ")))
fator = 1
i=1
while fator<N+1:
    fator *= i
    i+=1
print(f"O fatorial de {N} é {fator}")