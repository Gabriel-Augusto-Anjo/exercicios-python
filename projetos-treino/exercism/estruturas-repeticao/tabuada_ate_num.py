num = int(input("Número: "))
inicio = int(input("Início: "))
fim = int(input("Fim: "))

for i in range(inicio, fim + 1):
    print(f"{num} x {i} = {num * i}")
