vetor_a = [int(input()) for i in range(10)]
vetor_b = []

for i in range(10):
    if vetor_a[i] > 0:
        vetor_b.append(vetor_a[i])

if len(vetor_b) == 0:
    print("VETOR VAZIO")
else:
    print("Vetor A:")
    print(*vetor_a)
    
    print("Vetor B:")
    print(*vetor_b)
