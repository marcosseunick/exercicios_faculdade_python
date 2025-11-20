def contar_caixas(pilhas):
    if not pilhas:
        return 0
    else:
        return pilhas[0] + contar_caixas(pilhas[1:])