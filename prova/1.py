p=int(input("Digite um número: "))
soma=0
i=1
contador=0
while p>0:
    while i<=p:
        P=p
        P=p%10
        if P % i == 0:
            contador+=1
        i+=1
        if P<i:
            if contador==2:
                soma+=P
                p=p//10
                i=1
                contador=0
            if contador>2:
                p=p//10
                i=1
                contador=0
print("A soma dos números primos é:",soma)

