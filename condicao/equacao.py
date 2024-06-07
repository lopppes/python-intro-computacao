import math

def calcular_raizes(a, b, c):

    # Calculando o discriminante1

    discriminante = b ** 2 - 4 * a * c
    
    # Verificando se a equação tem raízes reais

    if discriminante < 0:
        print("A equação não tem raízes reais.")
    else:

        # Calculando as raízes usando a fórmula de Bhaskara

        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        
        # Imprimindo as raízes

        print("As raízes da equação são:")
        print("Raiz 1:", raiz1)
        print("Raiz 2:", raiz2)

# Coletando os coeficientes da equação quadrática

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

# Chamando a função para calcular e imprimir as raízes

calcular_raizes(a, b, c)
