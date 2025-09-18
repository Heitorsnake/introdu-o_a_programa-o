while 1==1:
    print("O P E R A Ç Õ E S   M A T E M Á T I C A S")
    print("***************M E N U*****************")
    print("1 - adição")
    print("2 - subtração")
    print("3 - divisão")
    print("4 - multiplicação")
    print("5 - par ou ímpar")
    print("6 - fatorial")
    print("7 - primo ou não")
    print("8 - sair")
    menu=int(input("digite aqui, qual das operações matemáticas você deseja fazer:"))
    if menu==1:
        num11=float(input("digite um número:"))
        num12=float(input("digite um número:"))
        num13=num11+num12
        print("a soma dos  dois números é:",num13)
        input("aperte qualquer tecla pra voltar para o menu")
    if menu==2:
        num21=float(input("digite um número:"))
        num22=float(input("digite um número:"))
        num23=num21-num22
        print("a subtração dos dois números é:",num23)
        input("aperte qualquer tecla pra voltar para o menu")
    if menu==3:
        num31=float(input("digite um número:"))
        num32=float(input("digite um número:"))
        num33=num31/num32
        print("a divisão dos dois número é:",num33)
        input("aperte qualquer tecla pra voltar para o menu")
        
    if menu==4:
        num41=float(input("digite um número:"))
        num42=float(input("digite um número:"))
        num43=num41*num42
        print("a mutiplicação dos dois número é:",num43)
        input("aperte qualquer tecla pra voltar para o menu")   
    if menu==5:
        num51=int(input("digite um número:"))
        if num51%2==0:
            print("o número é par")
            input("aperte qualquer tecla pra voltar para o menu")
        else:
            print("o número é ímpar")
            input("aperte qualquer tecla pra voltar para o menu")
    if menu==6:
        N = int(input("Digite um número: "))
        fator = 1
        i=1
        while i<N+1:
            fator *= i
            i+=1
            print(f"O fatorial de {N} é {fator}")
            input("aperte qualquer tecla pra voltar para o menu")
    if menu==7:
        p=int(input("Digite um número: "))
        c=0
        i=1
        while i<=p:
            if p % i == 0:
                c+=1
                i+=1
            if  c ==2:
                print("o número é primo!")
                input("aperte qualquer tecla pra voltar para o menu")
            else:
                print("o número não é primo")
                input("aperte qualquer tecla pra voltar para o menu")
    if menu ==8:
        print("até a proxima :)")
        break
    if menu !=(1,8):
        input("aperte enter para tentar novamente")
    if menu !=int:
        input("aperte enter para tentar novamente")
