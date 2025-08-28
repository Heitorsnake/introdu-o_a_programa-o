
anterior = 0
atual = 1
for i in range(25):
    print(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo