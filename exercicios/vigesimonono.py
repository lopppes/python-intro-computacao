def soma_elementos(lista):
    return sum(lista)

minha_lista = [1, 2, 3, 4, 5]
resultado = soma_elementos(minha_lista)
print(f"A soma dos elementos da lista (usando sum) é: {resultado}")

def soma_elementos(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

minha_lista = [1, 2, 3, 4, 5]
resultado = soma_elementos(minha_lista)
print(f"A soma dos elementos da lista (usando loop for) é: {resultado}")
