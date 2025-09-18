#conversor de Unidades em Módulo Reutilizável
# Enunciado: Crie um módulo com funções: celsius_p_fahrenheit, km_p_milhas, 
# kg_p_lb e a inversa de cada uma. Inclua validação e testes simples (doctest).
# Entrada (exemplo): km_p_milhas(5)
# Saída (exemplo): 3.106855.

def celsius_p_fahrenheit(celsius):
    '''
    >>> celsius_p_fahrenheit(20)
    68

    '''
    while True:
        try:
            fahrenheit = (celsius * (9/5)) + 32
            return fahrenheit
        except ValueError:
            print("Entrada inválida. Tente novamente.")

print(celsius_p_fahrenheit(20))