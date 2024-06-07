# Pergunta ao usuário quantas sequências ele deseja somar

total_sequencias = int(input("Quantas sequências de valores você deseja somar? "))

# Inicializando uma variável de contagem

contador = 0
soma = 0

# Repetir enquanto o contador for menor que o total de sequências especificado

while contador < total_sequencias:
    # Solicita ao usuário o valor da sequência atual e adiciona à soma total

    valor = int(input("Digite o valor da sequência: "))
    soma += valor
    contador += 1  # Incrementa o contador de sequências

# Mostra o total de valores somados

print("Total de valores somados:", soma)
