# Tipos de variáveis em Python:

# Números inteiros (int)
idade = 30
numero_filhos = 2

# Números de ponto flutuante (float)
peso = 70.5
altura = 1.75

# Texto (string)
nome = "João"
cidade = 'São Paulo'

# Booleanos (bool)
tem_fumante_em_casa = False
tem_cachorro = True

# Exemplo de cálculo de IMC (Índice de Massa Corporal):

# Fórmula do IMC: peso / (altura * altura)
# O resultado é uma medida de kg/m^2

# Definindo as variáveis para o cálculo do IMC
peso = 70.5  # em kg
altura = 1.75  # em metros

# Calculando o IMC
imc = peso / (altura ** 2)

# Exibindo o resultado
print("O IMC de uma pessoa com peso", peso, "kg e altura", altura, "m é:", imc)
