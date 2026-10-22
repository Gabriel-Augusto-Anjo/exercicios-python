valores = [int(input()) for _ in range(6)]  
par = 0
impar = 0

for i in range(6):
    if valores[i] % 2 == 0:
        par += 1
    else:
        impar += 1
        
print(f"\nValores: {valores}")
print(f"\nPares: {par}")        
print(f"Ímpares: {impar}")        
