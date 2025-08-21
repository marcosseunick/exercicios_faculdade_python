def validar_entrada(pin):
    alfabeto = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
    valor = str(input(pin))

    if len(valor) == 4:
        for digito in pin:
            if digito in alfabeto:
                return False
        return True
    
    elif len(valor) == 6:
        for digito in pin:
            if digito in alfabeto:
                return False
        return True
        
print(validar_entrada("Digite o Pin: "))