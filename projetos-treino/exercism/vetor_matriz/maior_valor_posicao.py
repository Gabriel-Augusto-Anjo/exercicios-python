vetor = [int(input())for i in range(8)]

indice = 0
maior = vetor[0]

for i in range(1,7):
    if vetor[i] > maior:
        maior = vetor[i]
        indice = i

print(f"Maior valor: {maior}")
print(f"Primeira posição: {indice}")        
