salario = float(input("Salário fixo: R$"))
total_vendido = float(input("Total vendido: R$"))

print(f"Comissão: R${total_vendido * 0.04}")
print(f"Salário total: R${salario + (total_vendido * 0.04)}")
