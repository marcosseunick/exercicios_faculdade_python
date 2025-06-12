# Dada uma sequência de letras minúsculas ('a' - 'z'),
# obtenha a distância máxima entre duas letras iguais
# e retorne essa distância junto com a letra que a
# formou.
# Caso exista mais de uma letra com a mesma
# distância máxima, retorne a que aparece primeiro.
# Exemplo:
# Para "fffffahhhhhhaaahhhhbhhahhhhabxx", a
# saída deve ser "a23".
# A distância máxima é formada pelo caracter 'a' de
# índice 5 ao índice 27 (baseado em 0). Portanto, a
# saída é "a23".

def distancia_maxima_caractere(sequencia):
    primeira_ocorrencia = {}
    ultima_ocorrencia = {}

    for i, char in enumerate(sequencia):
        if char not in primeira_ocorrencia:
            primeira_ocorrencia[char] = i
        ultima_ocorrencia[char] = i

    distancia_maxima = -1
    caractere_maxima = ''
    primeiro_indice_caractere_maxima = float('inf')
    
    for char in primeira_ocorrencia:
        distancia = ultima_ocorrencia[char] - primeira_ocorrencia[char]

        if distancia > distancia_maxima:
            distancia_maxima = distancia
            caractere_maxima = char
            primeiro_indice_caractere_maxima = primeira_ocorrencia[char]
        elif distancia == distancia_maxima:
            
            if primeira_ocorrencia[char] < primeiro_indice_caractere_maxima:
                caractere_maxima = char
                primeiro_indice_caractere_maxima = primeira_ocorrencia[char]

    return caractere_maxima + str(distancia_maxima)


sequencia_exemplo = "fffffahhhhhhaaahhhhbhhahhhhabxx"
resultado = distancia_maxima_caractere(sequencia_exemplo)
print(f"Para \"{sequencia_exemplo}\", a saída deve ser \"{resultado}\"")

sequencia_exemplo_2 = "abcdeabc"
resultado_2 = distancia_maxima_caractere(sequencia_exemplo_2)
print(f"Para \"{sequencia_exemplo_2}\", a saída deve ser \"{resultado_2}\"") 

sequencia_exemplo_3 = "abccba" 
resultado_3 = distancia_maxima_caractere(sequencia_exemplo_3)
print(f"Para \"{sequencia_exemplo_3}\", a saída deve ser \"{resultado_3}\"") 

sequencia_exemplo_4 = "banana" 
resultado_4 = distancia_maxima_caractere(sequencia_exemplo_4)
print(f"Para \"{sequencia_exemplo_4}\", a saída deve ser \"{resultado_4}\"") 