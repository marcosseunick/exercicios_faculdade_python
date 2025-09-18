def fahrenheit_p_celsius(fahrenheit):
    '''
    >>> fahrenheit_p_celsius(80)
    26.66

    '''
    while True:
        try:
            celsius = (fahrenheit - 32) * 5/9
            return f"{celsius:.2f}"
        except ValueError:
            print("Entrada inválida. Tente novamente")