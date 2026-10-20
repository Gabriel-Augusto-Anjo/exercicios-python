numeros = [int(input(f"Valor{i}: ")) for i in range(1, 6)]
soma = 0
for n in range(5):
    soma += numeros[n] 

print(f"Soma: {soma}")    
