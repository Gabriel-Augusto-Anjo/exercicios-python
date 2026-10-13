preco_unit = float(input("Preço unitário: R$"))
quant = int(input("Quantidade: "))
frete = float(input("Frete: R$"))
subtotal = round(preco_unit * quant, 2)
total = round((preco_unit * quant) + frete, 2)

print(f"Subtotal: R${subtotal:,.2f}")
print(f"Total: R${total:,.2f}")
