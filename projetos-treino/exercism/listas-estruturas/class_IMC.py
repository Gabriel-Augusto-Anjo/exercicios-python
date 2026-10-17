peso = int(input("Peso: "))
altura = float(input("Altura: "))

imc = float(peso / (altura * altura))

print(f"IMC: {imc:.2f}")
if imc < 18.5:
    print("Classificação: ABAIXO DO PESO")
elif imc >= 18.5 and imc < 25.0:
    print("Classificação: FAIXA NORMAL")
elif imc >= 25.0 and imc < 30:
    print("Classificação: ACIMA DA FAIXA")
else:
    print("Classificação: FAIXA ELEVADA")