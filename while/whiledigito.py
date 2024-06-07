# Solicita ao usuário um número inteiro

numero = int(input("Digite um número inteiro: "))

# Converte o número em uma string para iterar sobre seus dígitos

numero_str = str(numero)

# Inicializa a soma dos dígitos

soma_digitos = 0

# Inicializa o índice para percorrer os dígitos do número

indice = 0

# Repete enquanto ainda houver dígitos a serem somados

while indice < len(numero_str):

    # Adiciona o dígito atual à soma

    soma_digitos += int(numero_str[indice])

    # Incrementa o índice para passar para o próximo dígito

    indice += 1

# Exibe a soma dos dígitos

print("A soma dos dígitos de", numero, "é:", soma_digitos)
