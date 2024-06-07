def coeficiente_binomial(n, k):
    """
    Calcula o coeficiente binomial C(n, k), o número de combinações de "n" elementos
    tomados "k" a cada vez.

    Args:
    n (int): O número total de elementos.
    k (int): O número de elementos a serem escolhidos.

    Returns:
    int: O coeficiente binomial C(n, k).
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Utiliza a fórmula do coeficiente binomial: C(n, k) = C(n-1, k-1) + C(n-1, k)
    return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)

# Exemplo de uso
n = 5
k = 2
coef = coeficiente_binomial(n, k)
print("O coeficiente binomial C(", n, ",", k, ") é:", coef)


