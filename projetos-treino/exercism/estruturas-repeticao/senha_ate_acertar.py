senha = "1234"
cont = 0
while True:
    tentativa = str(input("Senha: "))
    cont += 1
    if tentativa == senha:
        break

    else:
        print("Senha incorreta.")


print("ACESSO LIBERADO")
print(f"Tentativas: {cont}")        
