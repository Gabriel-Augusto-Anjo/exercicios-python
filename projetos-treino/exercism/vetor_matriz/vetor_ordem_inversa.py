vetor = []

print("Entrada: ")

for i in range(8):
    valor = int(input())
    vetor.append(valor)

vetor.reverse()

print("Saída: ")
print(*vetor)    
