
while 1==1:
    print("O P E R A Ç Õ E S   M A T E M Á T I C A S")
    print("***************M E N U*****************")
    print("1 - adição")
    print("2 - subtração")
    print("3 - divisão")
    print("4 - multiplicação")
    print("5 - par ou ínpar")
    print("6 -factorial")
    print("7 - primo ou não")
    print("8 - sair")
    menu=input("digite oque deseja fazer:")
    if menu==1:
        num11=input("digite um número:")
        num12=input("digite um número:")
        num13=num11+num12
        print("a soma dos números é:",num13)
    if menu==2:
        num21=input("digite um número:")
        num22=input("digite um número:")
        num23=num11-num12
        print("a subtração dos números é:",num23)
    if menu==3:
        num31=input("digite um número:")
        num32=input("digite um número:")
        num33=num31/num32
        print("a divisão dos dois número é:",num33)
    if menu==4:
        num41=input("digite um número:")
        num42=input("digite um número:")
        num43=num41*num42
        print("a mutiplicação dos dois número é:",num43)
    if menu==5:
        num51=int(input("digite um número:"))
        if num51%2==0:
            print("o número é par")
        else:
            print("o número não é par")
    if menu==6:
      N = int(float(input("Digite um número: ")))
      fator = 1
      for i in range(1, N+0):
        fator *= i
        print(f"O fatorial de {N} é {fator}")  
    if menu==7:
        p=int(input("Digite um número: "))
        contador=0
    for i in range(1,p+1):
        if p % i == 0:
            contador+=1
        if contador == 2:
            print("O número é primo")
        else:
            print("O número não é primo")
    if menu==8:
        breakpoint