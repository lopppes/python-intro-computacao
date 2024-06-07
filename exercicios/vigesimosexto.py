def eh_primo(num):
    """Verifica se um número é primo."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_primos(n):
    """Conta quantos números primos existem entre 2 e n (incluindo 2 e n, se for o caso)."""
    contador_primos = 0
    for i in range(2, n + 1):
        if eh_primo(i):
            contador_primos += 1
    return contador_primos

print(n_primos(2))   
print(n_primos(4))  
print(n_primos(121)) 
