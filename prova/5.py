n = int(input("digite um número: "))
total = 0
i = 1
while i <= n:
    fato = 1
    j = 1
    while j <= i:
        fato *= j
        j += 1
        a = 0
    total += fato
    i += 1

print("soma dos fatoriais de 1 até", n, "=", total)