# Entrada dos dados com desempacotamento direto
a, b, c = [int(input(f"Lado {i+1}: ")) for i in range(3)]

print(f"Lados informados: {a}, {b} e {c}")

# Validação 1: Lados devem ser maiores que zero
# Validação 2: Desigualdade triangular (com ordenação implícita)
lados_ordenados = sorted([a, b, c])

if all(lado > 0 for lado in (a, b, c)) and (lados_ordenados[0] + lados_ordenados[1] > lados_ordenados[2]):
    print("Resultado: FORMAM UM TRIANGULO")
else:
    print("Resultado: NAO FORMAM UM TRIANGULO")