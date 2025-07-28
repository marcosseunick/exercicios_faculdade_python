def criptografar(frase: str) -> str:
    posicao = 0
    dicionario_criptografado = {}
    for letra in frase:
        if letra in dicionario_criptografado:
            dicionario_criptografado[letra].append(str(posicao))
        else:
            dicionario_criptografado[letra] = [str(posicao)]            
        posicao += 1

    # exibir(dicionario_criptografado)    

    texto_criptografado = ''
    for chave in dicionario_criptografado:
        texto_criptografado += chave + '='
        texto_criptografado += '&'.join(dicionario_criptografado[chave])
        texto_criptografado += '#'
           
    return texto_criptografado[:-1] + '@' + str(len(frase))

def exibir(dicionario):
    for item in dicionario:
        print(f'{item} - {dicionario[item]}')

def descriptografar(texto: str) -> str:
    frase = texto.split('@')
    tamanho = int(frase[1])

    fatiado = frase[0].split('#')
    dicionario = {}
    for fatia in fatiado:
        fatia_fatiada = fatia.split('=')
        dicionario[fatia_fatiada[0]] = fatia_fatiada[1].split('&')

    # exibir(dicionario)
    texto_descriptografado = [None] * tamanho
    for chave in dicionario:
        for posicao in dicionario[chave]:
            indice = int(posicao)
            texto_descriptografado[indice] = chave

    return ''.join(texto_descriptografado)

exemplo = 'A casa caiu'
cript = criptografar(exemplo)
print(cript)
descript = descriptografar(cript)
print(descript)