thanos = 150
aranha = 110
anos = 0

print(f"Antes: aranha = {aranha}, thanos = {thanos}")

if aranha > thanos:
    anos = 0
else:
    anos = (thanos - aranha) // (3 - 2) +1
    aranha += anos * 3
    thanos += anos * 2

print(f"Depois: aranha = {aranha}, thanos = {thanos}")
print(f"{anos} é a quantidade de anos que demorou para o aranha ultrapassar o thanos")
print(f"{aranha} é a altura do aranha")
print(f"{thanos} é a altura do thanos")
        
