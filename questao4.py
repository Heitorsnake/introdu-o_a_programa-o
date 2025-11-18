print=("******************************************")
print=("              ROBÔ AGRÍCULA             ")
print=("******************************************")

bateria = int(input("Digite o nível da bateria : "))
temperatura = int(input("Digite a temperatura em graus celsius : "))
umidade = int(input("Digite a umidade : "))
if bateria< 20: 
    print("Bateria muito baixa! Retorne imediatamente para a base.")
if bateria >= 20 and bateria<50: 
    print("bateria em nível moderado")
if bateria>50:
    print("bateria suficiente para operação")
if temperatura>40:
    print("Temperatura crítica! Operação suspensa")
if temperatura>5:
    if temperatura<40:
        print("temperatura adequada")
if temperatura<5:
    print("Frio extremo! Modo de economia ativado")
    
    
if umidade<30:
    print("Solo muito seco. Recomendado iniciar irrigação")
if umidade>30:
    if umidade<80:
        print("umidade em nível adequado")
if umidade>80:
    print("Solo encharcado! Suspenda irrigação imediatamente")

autorizado=0

if bateria >= 50 :
    if temperatura >= 10 :
        if temperatura <= 35 :
            if umidade >= 30 :
                if umidade <= 80:
                    autorizado+=1
if autorizado == 1:
    print("Robô autorizado a iniciar a operação!")
    acao = input("Digite a ação desejada : ")
    autorizado+=1
else :
    print("Operação negada! Verifique as condições do ambiente.")


if autorizado == 2:
    if acao == "plantio":
        print("Iniciando modo PLANTIO...")
    if acao == "colheita":
        print("Iniciando modo COLHEITA...")
    if acao == "irrigacao":
        print("Iniciando modo IRRIGAÇÃO...")
    autorizado=0