soma = 0
quant = 0
maior18 = 0

while True:
    idade = int(input("Idade: "))
    if idade >= 0:
        soma += idade
        quant += 1
        if idade >= 18:
            maior18 += 1
    else:
        break

if quant == 0:
    print("NENHUMA IDADE INFORMADA")
else:
    media = float(soma / quant)

    print(f"Quantidade: {quant}")
    print(f"Média: {media}")    
    print(f"Maiores de idade: {maior18}")
