num = int(input("Número: "))

if num % 3 == 0 or num % 5 == 0:
    if num % 3 == 0 and num % 5 == 0:
        print("DIVISÍVEL POR 3 E 5")
    elif num % 3 == 0:
        print("DIVISIVEL APENAS POR 3")
    else:
        print("DIVISÍVEL APENAS POR 5")
else:
    print("NÃO DIVISÍVEL POR 3 NEM 5")