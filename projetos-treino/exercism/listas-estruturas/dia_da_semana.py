from unittest import case

try:
    num = int(input("Digite um número de 1 a 7: "))

    match num:
        case 1:
            print("SEGUNDA-FEIRA")
        case 2:
            print("TERÇA-FEIRA")
        case 3:
            print("QUARTA-FEIRA")
        case 4:
            print("QUINTA-FEIRA")
        case 5:
            print("SEXTA-FEIRA")
        case 6:
            print("SÁBADO")
        case 7:
            print("DOMINGO")
        case _:
            print("OPÇÃO INVÁLIDA (Número fora do intervalo 1-7)")

except ValueError:
    print("OPÇÃO INVÁLIDA (Por favor, digite apenas números inteiros)")