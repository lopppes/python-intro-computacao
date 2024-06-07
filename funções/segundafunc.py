def calcular_fatorial(numero):
    """
    Calcula o fatorial de um número.

    Args:
    numero (int): O número para o qual calcular o fatorial.

    Returns:
    int: O fatorial do número.
    """
    if numero == 0 or numero == 1:  # Caso base: fatorial de 0 e 1 é 1
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)  # Recursivamente calcula o fatorial

# Exemplo de uso
numero = 5
fatorial = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", fatorial)
