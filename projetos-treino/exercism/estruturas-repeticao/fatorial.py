n = int(input("Número: "))

def n_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * n_fatorial(n - 1)    

print(n_fatorial(n))        
