from datetime import datetime

# Pergunta ao usuário o ano de nascimento
ano_nascimento = input("Em que ano você nasceu? (Formato: YYYY) ")

# Pergunta ao usuário o mês de nascimento
mes_nascimento = input("Em que mês você nasceu? (Formato: MM) ")

# Pergunta ao usuário o dia de nascimento
dia_nascimento = input("Em que dia você nasceu? (Formato: DD) ")

# Obtém a data atual
data_atual = datetime.now()

# Cria um objeto datetime com a data de nascimento fornecida pelo usuário
data_nascimento = datetime(int(ano_nascimento), int(mes_nascimento), int(dia_nascimento))

# Calcula a diferença entre a data atual e a data de nascimento para obter a idade
idade = data_atual - data_nascimento

# Calcula o número de dias, meses e anos de vida
anos = idade.days // 365
meses = (idade.days % 365) // 30
dias = (idade.days % 365) % 30

# Imprime a idade em anos, meses e dias
print("Você tem", anos, "anos,", meses, "meses e", dias, "dias de vida.")
