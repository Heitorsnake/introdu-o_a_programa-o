p=int(input("Digite um número: "))
contador=0
i=1
while i<=p:
    if p % i == 0:
        contador+=1
    i+=1
if contador ==2:
    print("o número é primo!")
else:
    print("o número não é primo")