def possui_adjacente_igual(numero):
    numero_str = str(numero)
    i = 0
    while i < len(numero_str) - 1:
        if numero_str[i] == numero_str[i + 1]:
            return True
        i += 1
    return False

def main():
    numero = int(input("Digite um número inteiro: "))
    if possui_adjacente_igual(numero):
        print("sim")
    else:
        print("não")

if __name__ == "__main__":
    main()
