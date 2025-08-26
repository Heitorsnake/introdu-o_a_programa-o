n = int(float(input("Digite um número: ")))
eh_primo = True
if n < 2:
    eh_primo = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            eh_primo = False
            break
if eh_primo:
    print("O número é primo")
else:
    print("O número não é primo")