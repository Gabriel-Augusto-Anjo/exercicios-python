import statistics

notas = [float(input(f"Nota{i}: ")) for i in range(1, 11)]

media = statistics.mean(notas)

print(f"Média: {media}")
