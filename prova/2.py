num = int(input("Digite um número: "))
hexa = hex(num)
print(f"O número {num} em hexadecimal é {hexa}")
p = num
i = 1
contador = 0
if num == 0:
    binario = "0"
else:
    binario = ""
    n = num
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2
        contador += 1

print(f"O número {num} em binário é {binario}")

