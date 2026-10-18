imovel = float(input("Valor do imóvel: "))
salario = float(input("Salário: "))
prazo = int(input("Prazo: "))

prestacao = float(imovel / (prazo * 12))

limite = float(salario * 0.30)

if limite >= prestacao:
    result = "APROVADO"
else:
    result = "NEGADO"

print(f"Prestação: R${prestacao:.2f}")
print(f"Limite: R${limite:.2f}")
print(f"Resultado: {result}")