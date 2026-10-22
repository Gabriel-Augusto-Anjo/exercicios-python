valores = [int(input()) for _ in range(8)]
pos = 0
neg = 0
zero = 0
for i in range(8):
    if valores[i] > 0:
        pos += 1
    elif valores[i] < 0:
        neg += 1
    else:
        zero += 1     

print(f"Positivos: {pos}")        
print(f"Negativos: {neg}")        
print(f"Zeros: {zero}")      
