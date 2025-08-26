p=int(input("Digite um número: "))
contador=0
for i in range(1,p+1):
    if p % i == 0:
        contador+=1
if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")
