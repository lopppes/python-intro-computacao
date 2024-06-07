def decompor_em_fatores_primos(n):
    fatores = {}
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            if divisor in fatores:
                fatores[divisor] += 1
            else:
                fatores[divisor] = 1
            n //= divisor
        divisor += 1

    return fatores

def mostrar_fatores_primos():
   
    numero = int(input("Digite um número inteiro maior que 1: "))
    
    if numero <= 1:
        print("O número deve ser maior que 1.")
        return

    
    fatores_primos = decompor_em_fatores_primos(numero)
    
  
    print(f"A decomposição em fatores primos de {numero} é:")
    for fator, multiplicidade in fatores_primos.items():
        print(f"Fator: {fator}, Multiplicidade: {multiplicidade}")


mostrar_fatores_primos()
