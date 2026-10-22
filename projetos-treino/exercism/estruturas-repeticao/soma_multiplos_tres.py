a = int(input("A: "))
b = int(input("B: "))
soma = 0
if a > b:
    a, b = b, a


for i in range(a, b+1):
    if i % 3 == 0:
        soma += i

print(f"Soma dos múltiplos de 3: {soma}")       
