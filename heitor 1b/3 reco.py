N = int(float(input("Digite um número: ")))
soma = 0
m=1
while N >0:
    if N>m:
        m+=m
print("A soma dos números inteiros de 1 a", N, "é:", m)