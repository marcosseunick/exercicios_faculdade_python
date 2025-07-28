def contador_vogais(string):
    vogais = "aeiou"
    contador = 0
    for letra in string:
        if letra in vogais:
            contador += 1
    return contador