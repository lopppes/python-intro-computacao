def calcular_media(lista):
    """
    Calcula a média de uma lista de números.

    Args:
    lista (list): Uma lista de números.

    Returns:
    float: A média dos números na lista.
    """
    total = sum(lista)  # Soma todos os números na lista
    media = total / len(lista)  # Divide a soma pelo número de elementos na lista
    return media

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
media = calcular_media(numeros)
print("A média é:", media)
