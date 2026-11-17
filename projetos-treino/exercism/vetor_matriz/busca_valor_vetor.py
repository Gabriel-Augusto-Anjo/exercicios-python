vetor = [int(input()) for i in range(10)]
posicoes = []

valor = int(input("Valor procurado: "))

for i in range(10):
    if vetor[i] == valor:
        posicoes.append(i)

if len(posicoes) == 0:
    print("NÃO ENCONTRADO")
else:
    print(f"Posições: {posicoes}")

