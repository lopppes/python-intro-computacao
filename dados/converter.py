# Solicita ao usuário que insira o número de segundos a serem convertidos e armazena o valor na variável 'segundos'
segundos = input("Por favor, entre com o número de segundos que deseja converter: ")

# Converte a entrada do usuário (uma string) em um número inteiro (int) e armazena na variável 'totalSegundos'
totalSegundos = int(segundos)

# Calcula o número de horas, minutos e segundos a partir do total de segundos
# Divide o total de segundos pelo número de segundos em uma hora (3600) para obter o número de horas
horas = totalSegundos // 3600
# Calcula o número de segundos restantes após a divisão pelas horas
segundosRestantes = totalSegundos % 3600
# Divide os segundos restantes pelo número de segundos em um minuto (60) para obter o número de minutos
minutos = segundosRestantes // 60
# Calcula os segundos restantes após a divisão pelos minutos
segundosRestantesFinal = segundosRestantes % 60

# Verifica se o tempo total é maior ou igual a um dia (86400 segundos)
if totalSegundos >= 86400:
    # Se for maior ou igual a um dia, calcula o número de dias e ajusta os segundos restantes
    dias = totalSegundos // 86400
    horas -= dias * 24  # Subtrai as horas equivalentes aos dias calculados
    print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosRestantesFinal, "segundos.")
else:
    # Se for menor do que um dia, imprime apenas horas, minutos e segundos
    print(horas, "horas,", minutos, "minutos e", segundosRestantesFinal, "segundos.")
