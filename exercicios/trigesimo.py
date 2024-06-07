def maior_elemento(lista):
    if not lista:
        raise ValueError("A lista está vazia")
    
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

lista_de_numeros = [1, 3, 5, 7, 2, 8, 6]
print(maior_elemento(lista_de_numeros)) 
