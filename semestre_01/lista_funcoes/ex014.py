def descriptografar_string(string_criptografada):

    partes = string_criptografada.split('#')
    tamanho_maximo = 0
    posicoes_caracteres = []

   
    for parte in partes:
        if '=' in parte:
            caractere, posicoes_str = parte.split('=', 1)
            posicoes = [int(p) for p in posicoes_str.split('&')]
            posicoes_caracteres.append((caractere, posicoes))
            if posicoes:
                tamanho_maximo = max(tamanho_maximo, max(posicoes) + 1)
        else:
            
            pass

   
    if tamanho_maximo == 0:
        return ""

   
    frase_reconstruida = [''] * tamanho_maximo

    for char, posicoes in posicoes_caracteres:
        for pos in posicoes:
            if 0 <= pos < tamanho_maximo:
                frase_reconstruida[pos] = char


    return "".join(frase_reconstruida)