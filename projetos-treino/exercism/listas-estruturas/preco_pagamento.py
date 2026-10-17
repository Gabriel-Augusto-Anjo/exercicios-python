preco = float(input("Preço: R$"))
opcao = int(input("Opção: "))

match opcao:
    case 1:
        final = round(preco - (preco * 0.1), 2)

    case 2:
        final = round(preco - (preco * 0.05), 2)

    case 3:
        final = round(preco, 2)

    case 4:
        final = round(preco + (preco * 0.08), 2)

    case _:
        print("Digite uma opção válida")

print(f"Valor final: R${final:,.2f}")