def subir_escada(degraus):

    if degraus <= 1:
        return 1
    
    else:
        return subir_escada(degraus - 1) + subir_escada(degraus - 2)

