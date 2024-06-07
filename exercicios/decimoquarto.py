def imprimir_impares(n):
    contador = 0
    numero = 1
    while contador < n:
        print(numero)
        numero += 2
        contador += 1

def main():
    n = int(input("Digite o valor de n: "))
    imprimir_impares(n)

if __name__ == "__main__":
    main()
