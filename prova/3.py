#lei de formação da sequencia ,1,1,2,3,5,8,13,21
n=int(input("Digite um número: "))
a=0
b=1
contador=0
while contador<n:
    print(a)
    c=a+b
    a=b
    b=c
    contador+=1
