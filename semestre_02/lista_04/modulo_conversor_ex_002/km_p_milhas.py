def km_p_milhas(km):
    '''
    >>> km_p_milhas(50)
    31.25

    '''
    while True:
        try:
            milhas = km/1.6
            return milhas
        except ValueError:
            print("Entrada inválida. Tente novamente.")