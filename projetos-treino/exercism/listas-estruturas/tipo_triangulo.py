# Entrada de dados
a, b, c = [int(input(f"Lado {i + 1}: ")) for i in range(3)]

# Ordenação para validar a existência do triângulo
menor1, menor2, maior = sorted([a, b, c])

# Atribuição booleana direta
eh_triangulo = (menor1 > 0) and (menor1 + menor2 > maior)

# Classificação direta baseada na condição
if eh_triangulo:
    if a == b == c:  # Encadeamento direto de igualdade do Python
        tipo = "EQUILÁTERO"
    elif a == b or b == c or a == c:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"
else:
    tipo = "NÃO FORMA UM TRIÂNGULO"

# Saída
print(f"Lados: {a}, {b}, {c}")
print(f"Resultado: {tipo}")