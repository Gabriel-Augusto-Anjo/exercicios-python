try:
    quant_termos = int(input("Quantidade de termos: "))
except ValueError:
    print("Digite um valor inteiro válido.")
else:
    if quant_termos < 2:
        print("Digite um número maior ou igual a dois.")
    else:
        termos = []
        f0, f1 = 0, 1
        
        # O loop roda exatamente a quantidade de vezes desejada
        for _ in range(quant_termos):
            termos.append(f0)
            # Atualização simultânea (evita lógica complexa de índices)
            f0, f1 = f1, f0 + f1
            
        print(*termos)
