#Faça um algoritmo que receba um número inteiro, representando uma quantidade em segundos e exiba um texto 
#informando o total de dias, horas, minutos e segundos, quando houver um destes. Por exemplo.

def converter_segundos(segundos):
    dias = segundos // 86400 
    segundos %= 86400
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60

    resultado = []
    if dias > 0:
        resultado.append(f"{dias} dia{'s' if dias > 1 else ''}")
    if horas > 0:
        resultado.append(f"{horas} hora{'s' if horas > 1 else ''}")
    if minutos > 0:
        resultado.append(f"{minutos} minuto{'s' if minutos > 1 else ''}")
    if segundos > 0 or not resultado:  # Se não houver outros, exibe os segundos
        resultado.append(f"{segundos} segundo{'s' if segundos > 1 else ''}")

    return ", ".join(resultado)

segundos = int(input("Digite o número de segundos: "))
resultado = converter_segundos(segundos)
print(resultado)