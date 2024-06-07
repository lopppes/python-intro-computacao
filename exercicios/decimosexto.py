def verificar_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

def main():
    numero = int(input("Digite um número inteiro: "))
    if verificar_primo(numero):
        print("primo")
    else:
        print("não primo")

if __name__ == "__main__":
    main()
