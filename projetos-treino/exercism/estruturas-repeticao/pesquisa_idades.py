import statistics

idades = [int(input()) for _ in range(10)]

menor18 = 0
maior60 = 0

for i in range(10):
    if idades[i] < 18:
        menor18 += 1
    elif idades[i] >= 60:
        maior60 += 1

print(f"\nMédia: {statistics.mean(idades)}")        
print(f"Menores de 18: {menor18}")        
print(f"Com 60 anos ou mais: {maior60}")        
