
try:
    num_mes = int(input("Digite o número de 1 a 12: "))
    ano = int(input("Digite o ano: "))

    if num_mes >= 1 and num_mes <= 12:
            if num_mes in (1, 3, 5, 7, 8, 10, 12):
                print("31 dias")
            elif num_mes in (4, 6, 9, 11):
                print("30 dias")
            elif num_mes == 2 and ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
                print("29 dias")
            else:
                print("28 dias")
    else:
        print("MÊS INVÁLIDO, DIGITE UM NÚMERO ENTRE 1 E 12")
except ValueError:
    print("Digite um número inteiro válido")