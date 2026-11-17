vetor = [int(input())for i in range(8)]

indice = 0
menor = vetor[0]

for i in range(1,7):
    if vetor[i] < menor:
        menor = vetor[i]
        indice = i

print(f"Menor valor: {menor}")
print(f"Primeira posição: {indice}")        
