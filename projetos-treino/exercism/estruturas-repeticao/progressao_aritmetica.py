termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
quant = int(input("Quantidade: "))

seq = [termo]
soma = termo

for i in range(quant-1):
    prox = seq[i] + razao
    soma += prox
    seq.append(prox)

print(f"Sequência: {seq}")
print(f"Soma: {soma}")    
