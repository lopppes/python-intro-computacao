def inverter_sequencia():
    numeros = []
    
    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        numeros.append(numero)
    
    for numero in reversed(numeros):
        print(numero)

inverter_sequencia()
