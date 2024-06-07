def verifica_adjacentes_iguais(numero):
    numero_str = str(numero)

    for i in range(len(numero_str) - 1):
        if numero_str[i] == numero_str[i + 1]:
            return True
    return False

def main():
    numero = input("Digite um número: ")
    
    try:
        numero = int(numero)
        if verifica_adjacentes_iguais(numero):
            print("O número contém dígitos adjacentes iguais.")
        else:
            print("O número não contém dígitos adjacentes iguais.")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
