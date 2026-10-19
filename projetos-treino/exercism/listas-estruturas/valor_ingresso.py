idade = int(input("Idade: "))
estuda = str(input("Estudante: "))
ingresso = round(float(30), 2)

if idade < 12 or estuda.lower() == "sim"  or idade >= 60:
    ingresso = ingresso - (ingresso * 0.5)

print(f"Valor do ingresso: R${ingresso:.2f}")
