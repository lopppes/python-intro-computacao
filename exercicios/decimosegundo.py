import math

a = float(input("Digite o coeficiente 'a' da equação: "))
b = float(input("Digite o coeficiente 'b' da equação: "))
c = float(input("Digite o coeficiente 'c' da equação: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"a raiz desta equação é {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 == raiz2:
        print(f"a raiz dupla desta equação é {raiz1}")
    else:
        raiz1, raiz2 = min(raiz1, raiz2), max(raiz1, raiz2)
        print(f"as raízes da equação são {raiz1} e {raiz2}")
