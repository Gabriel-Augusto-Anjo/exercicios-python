try:
    n = int(input("N: "))
except ValueError:
    print("Digite um número inteiro positivo")
else:
    soma = 0
    for i in range(1,n+1):
        soma += i
        
    print(f"Soma: {soma}")    
