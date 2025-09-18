def kg_p_lb(kg):
    '''

    >>> kg_p_lb(50)
    110.25

    '''

    while True:
        try:
            lb = kg * 2.205
            return lb
        except ValueError:
            print("Entrada inválida. Tente novamente.")
