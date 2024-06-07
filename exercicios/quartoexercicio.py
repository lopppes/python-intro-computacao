def contaSegundos(segundos):
    dias = segundos // (24 * 3600)
    segundos_rest = segundos % (24 * 3600)
    horas = segundos_rest // 3600
    segundos_rest %= 3600
    minutos = segundos_rest // 60
    segundos_rest %= 60
    
    return dias, horas, minutos, segundos_rest

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias, horas, minutos, segundos_rest = contaSegundos(segundos)

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_rest} segundos.")
