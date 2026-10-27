soma = 0
maior = 0
quant = 0

while True:
    preco = float(input("Preços: "))
    
    if preco == 0:
        break
    else:
        quant += 1
        soma += preco
        if preco > maior:
            maior = preco
            
if quant == 0:
    print("NENHUM PRODUTO INFORMADO")
else:
    print(f"Produtos: {quant}")                
    print(f"Total: R${soma:.2f}")                
    print(f"Maior preço: R${maior:.2f}")      
