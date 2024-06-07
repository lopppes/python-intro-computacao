def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def main():
    n = int(input("Digite o valor de n: "))
    resultado = calcular_fatorial(n)
    print(resultado)

if __name__ == "__main__":
    main()
