vetor = []
soma = 0

print("Vetor: ")

for i in range(10):
    valor = float(input())
    vetor.append(valor)
    soma += vetor[i]

print("Soma: ", int(soma))
