tentativas = 0

while True:
    nota = int(input("Nota: "))
    if (nota >= 0) and (nota <= 10):
        break
    else:
        tentativas += 1
        print("Valor inválido.")

print(f"Nota aceita: {nota}")            
print(f"Tentativas inválidas: {tentativas}")            
