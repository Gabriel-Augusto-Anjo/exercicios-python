import statistics

alturas = [float(input()) for _ in range(8)]

print(f"Média: {round(statistics.mean(alturas), 2)} m")
print(f"Maior: {max(alturas):2f} m")
print(f"Menor: {min(alturas):2f} m")
