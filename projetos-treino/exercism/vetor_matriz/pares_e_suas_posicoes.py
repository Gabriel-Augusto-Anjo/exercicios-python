vetor = [1, 3, 0, 7, 9]
def encontrar_par(vetor):
    for i in range(1, len(vetor)):
        if vetor[i] % 2 == 0:
            return True
        

print("Vetor:")
print(*vetor)

if encontrar_par(vetor):
    print("\nPares encontrados: ")
    for i in range(1, len(vetor)):
        if vetor[i] % 2 == 0:
            print(f"{vetor[i]} -- posição {i}")
else: 
    print("NENHUM VALOR PAR.")            

