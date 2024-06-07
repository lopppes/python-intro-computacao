# lista
frutas = ["maçã", "banana", "laranja", "uva"]

# acessando elementos da lista

primeira_fruta = frutas[0]  # Acessa o primeiro elemento (índice 0)
print(f"A primeira fruta é: {primeira_fruta}")

# adicionando elementos à lista

frutas.append("morango")  # Adiciona "morango" ao final da lista
print("Após adicionar uma fruta:", frutas)

# removendo elementos da lista
frutas.remove("banana")  # Remove "banana" da lista
print("Após remover uma fruta:", frutas)

# iterando sobre a lista
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)

# outras operações comuns em listas
# Ordenando a lista
frutas.sort()
print("Lista de frutas ordenada:", frutas)

# obtendo o tamanho da lista
tamanho = len(frutas)
print(f"O número de frutas na lista é: {tamanho}")

# verificando a existência de um elemento na lista
existe_maca = "maçã" in frutas
print(f"Existe maçã na lista? {existe_maca}")
