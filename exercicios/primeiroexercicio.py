def calcular_quadrado(lado):

    # Calcula o perímetro do quadrado (4 vezes o lado)

    perimetro = 4 * lado

    # Calcula a área do quadrado (lado ao quadrado)

    area = lado ** 2

    # Retorna o perímetro e a área como uma tupla

    return perimetro, area

def main():

    # Solicita ao usuário o valor do lado do quadrado

    lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))
    
    # Calcula o perímetro e a área do quadrado usando a função calcular_quadrado

    perimetro, area = calcular_quadrado(lado)
    
    # Imprime o resultado no formato solicitado
    
    print(f"perímetro: {perimetro} - área: {area}")

if __name__ == "__main__":
    main()
