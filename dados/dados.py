# Solicita ao usuário que insira uma temperatura em Fahrenheit e armazena o valor na variável temperaturaFahrenheit
temperaturaFahrenheit = input("Digite uma temperatura em Fahrenheit: ")

# Converte a temperatura de Fahrenheit para Celsius
# Primeiro, converte a entrada do usuário (uma string) em um número de ponto flutuante (float)
# Em seguida, aplica a fórmula de conversão de Fahrenheit para Celsius: (F - 32) * 5/9
temperaturaCelsius = (float(temperaturaFahrenheit) - 32) * 5 / 9

# Imprime a temperatura convertida para Celsius
print("A temperatura em Celsius é: ", temperaturaCelsius)
