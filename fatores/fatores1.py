import math

def calcular_fatoriais():
    # Solicita ao usuário que digite uma sequência de números
    numeros_str = input("Digite uma sequência de números separados por espaço: ")
    
    # Converte a string de números para uma lista de inteiros
    numeros = list(map(int, numeros_str.split()))
    
    # Calcula o fatorial de cada número e exibe o resultado
    for numero in numeros:
        fatorial = math.factorial(numero)
        print(f"O fatorial de {numero} é {fatorial}")

# Executa a função
calcular_fatoriais()
