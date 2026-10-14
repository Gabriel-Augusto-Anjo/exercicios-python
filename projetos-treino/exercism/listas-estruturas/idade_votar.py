idade = int(input("Informe sua idade: "))

if idade < 16:
  print("NÃO PODE VOTAR")
elif idade < 18 or idade >= 70:
  print("VOTO OPCIONAL")
else:
  print("VOTO OBRIGATÓRIO")
  
