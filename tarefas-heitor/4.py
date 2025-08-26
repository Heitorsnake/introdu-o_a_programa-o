j=int(input("digite o numero de jogadores: "))
altura = 0
for i in range(j):
    altura += float(input("escreva a altura dos jogadores: "))
media = altura / j
print("A média de altura dos jogadores é:", media)
