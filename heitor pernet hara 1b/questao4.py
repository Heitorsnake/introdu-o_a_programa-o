bateria=(input("Digite o nível da bateria : "))
temperatura=int(input("Digite a temperatura em graus celcius : "))
umidade=int(input("Digite a umidade : "))
ação=input("Digite a ação desejada : ")
if bateria<20: 
    print("Bateria muito baixa! Retorne imediatamente para a base.")
if bateria>=20:
    print("atenção bateria em nível moderado")
if bateria<50:
    print("atenção bateria em nível moderado")