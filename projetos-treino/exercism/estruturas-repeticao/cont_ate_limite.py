try:
    n = int(input("N: "))
except ValueError as err:
    print("Digite um número inteiro")
else:
    num = [int(i + 1) for i in range(n)]
    print(*num)   
