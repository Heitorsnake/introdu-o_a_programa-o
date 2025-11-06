num_jogadores = int(input("Escreva o número de jogadores: "))
soma_altura_f = 0
soma_altura_m = 0
soma_peso_f = 0
soma_peso_m = 0
contador = 0
soma_idade = 0
maior_altura_f = 0  
maior_peso_m = 0

while contador < num_jogadores:
    sexo = input("Informe o gênero do jogador (M/F): ")
    if sexo == "M":
        soma_altura_m += float(input("Informe a altura do jogador: "))
        peso_m = float(input("Informe o peso do jogador: "))
        soma_peso_m += peso_m
        if peso_m > maior_peso_m:
            maior_peso_m = peso_m
        soma_idade += int(input("Informe a idade do jogador: "))
    if sexo == "F":
        altura_f = float(input("Informe a altura da jogadora: "))
        soma_altura_f += altura_f
        if altura_f > maior_altura_f:
            maior_altura_f = altura_f
        peso_f = float(input("Informe o peso do jogadora: "))
        soma_peso_f += peso_f
        soma_idade += int(input("Informe a idade do jogadora: "))
    contador += 1

media_idade = soma_idade / num_jogadores
if num_jogadores > 0:
    print("Média de idade dos jogadores:", media_idade)

    if maior_altura_f > 0:
        print("A jogadora mais alta tem altura:",maior_altura_f)
    else:
        print("Nenhuma jogadora mostrado")

    if maior_peso_m > 0:
        print("O jogador masculino mais pesado tem peso:",maior_peso_m)
    else:
        print("Nenhum jogador masculino mostrado")
