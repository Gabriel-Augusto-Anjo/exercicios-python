vetor = [int(input()) for i in range(10)]

valor = int(input("Valor procurado: "))

ocorrencias = 0
for i in range(10):
    if vetor[i] == valor:
        ocorrencias += 1

print(f"Ocorrências: {ocorrencias}")        
