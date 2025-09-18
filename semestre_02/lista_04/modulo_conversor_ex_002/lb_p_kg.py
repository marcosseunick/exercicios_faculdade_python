def lb_p_kg(lb):
    '''

    >>> lb_p_kg(50)
    22.6796

    '''
    while True:
        try:
            kg = lb / 2.205
            return kg
        except ValueError:
            print("Entrada inválida. Tente novamente")