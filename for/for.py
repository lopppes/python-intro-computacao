# impressão de Números de 0 a 9
print("Exemplo 1: Impressão de Números de 0 a 9")
# usando o range(10) para gerar números de 0 a 9
for i in range(10):
    # imprime o valor atual de i
    print(i)

print("\n")  # linha em branco para separar os exemplos

# soma dos Primeiros 10 Números
print("Exemplo 2: Soma dos Primeiros 10 Números")
# inicializa a variável de soma
soma = 0

# usa o range(1, 11) para gerar números de 1 a 10
for i in range(1, 11):
    # adiciona o valor atual de i à variável soma
    soma += i

# imprime o resultado da soma
print("A soma dos primeiros 10 números é:", soma)

print("\n")  # linha em branco para separar os exemplos

# impressão de Números Pares de 0 a 18
print("Exemplo 3: Impressão de Números Pares de 0 a 18")
# usa o range(0, 20, 2) para gerar números pares de 0 a 18
for i in range(0, 20, 2):
    # imprime o valor atual de i
    print(i)

print("\n")  # linha em branco para separar os exemplos

# iterando Sobre uma Lista
print("Exemplo 4: Iterando Sobre uma Lista")
# define uma lista de frutas
frutas = ["maçã", "banana", "cereja", "damasco"]

# usa o range(len(frutas)) para iterar sobre os índices da lista
for i in range(len(frutas)):
    # imprime o índice e o valor correspondente na lista
    print(i, frutas[i])
