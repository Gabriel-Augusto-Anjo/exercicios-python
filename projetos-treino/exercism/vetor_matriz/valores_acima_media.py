TOTAL_NOTAS = 8
notas = []

print("Digite as notas:")
for i in range(TOTAL_NOTAS):
    # Usando float para aceitar decimais e adicionando um prompt descritivo
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

# sum() calcula a soma da lista de forma nativa e limpa
media = sum(notas) / TOTAL_NOTAS

# List comprehension para filtrar valores acima da média de forma elegante
acima_media = [nota for nota in notas if nota > media]

print(f"\nMédia: {media:.2f}")

if acima_media:
    print(f"Acima da média: {acima_media}")
    # len() substitui a necessidade da variável 'quant'
    print(f"Quantidade: {len(acima_media)}")
else:
    print("Nenhum valor acima da média.")
