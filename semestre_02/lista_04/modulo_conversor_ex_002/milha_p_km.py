def milhas_p_km(milhas):
    '''
    >>> milhas_p_km(50)
    80

    '''
    while True:
        try:
            km = milhas * 1.6
            return milhas
        except ValueError:
            print("Entrada inválida. Tente novamente.")