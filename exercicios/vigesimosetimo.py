import math

def eh_hipotenusa(h):
    """Verifica se um número é a hipotenusa de algum triângulo retângulo com lados inteiros."""
    for i in range(1, h):
        for j in range(1, h):
            if i * i + j * j == h * h:
                return True
    return False

def soma_hipotenusas(n):
    """Calcula a soma de todas as hipotenusas de triângulos retângulos com catetos inteiros entre 1 e n."""
    soma = 0
    for h in range(1, n + 1):
        if eh_hipotenusa(h):
            soma += h
    return soma


print(soma_hipotenusas(25)) 
print(soma_hipotenusas(10)) 
