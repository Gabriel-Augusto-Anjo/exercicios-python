soma = 0
quant = 0

while True:
    valor = int(input("Valor: "))
    if valor != 0:
        soma += valor
        quant += 1
    else:
        break

if quant == 0:
    print("NENHUM VALOR VÁLIDO")
else:
    media = float(soma / quant)

    print(f"Quantidade: {quant}")
    print(f"Soma: {soma}")
    print(f"Média: {media}")    
