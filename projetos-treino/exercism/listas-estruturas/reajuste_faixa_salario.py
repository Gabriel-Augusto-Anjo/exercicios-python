salario = float(input("Salário: R$"))

if salario <= 1500.00:
    percent = 0.15

elif salario <= 3000.00:
    percent = 0.1

else:
    percent = 0.05

print(f"Percentual: {int(percent * 100)}%")
print(f"Novo salário: R${salario + (salario * percent):,.2f}")