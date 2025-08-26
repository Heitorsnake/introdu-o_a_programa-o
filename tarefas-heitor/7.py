thanos = 150
aranha = 110
for i in range(100):
    thanos = thanos + 2
    aranha = aranha + 3
    if aranha > thanos:
        print(f"{i} é a quantidade de anos que demorou para o aranha ultrapassar o thanos")
        print(f"{aranha} é a altura do aranha")
        print(f"{thanos} é a altura do thanos")
        break
        
        