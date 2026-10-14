ano = int(input("Ano: "))
ultimos_dois_str = str(ano)[-2:]

if ano % 4 == 0 and ultimos_dois_str != "00":
  print("Resultado: ANO BISSEXTO")
elif ultimos_dois_str == "00" and ano % 400 == 0:
  print("Resultado: ANO BISSEXTO")
else:
  print("Resultado: NÃO BISSEXTO")
