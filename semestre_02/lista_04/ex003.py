import string
from collections import Counter

def limpar_texto(texto: str) -> str:

    texto_lower = texto.lower()

    texto_limpo = ""
    for char in texto_lower:
        if char not in string.punctuation:
            texto_limpo += char
            
    return texto_limpo

def analisar_frequencia(texto: str, n: int = 10) -> list:

    texto_limpo = limpar_texto(texto)
   
    palavras = texto_limpo.split()
   
    contador_palavras = Counter(palavras)
 
    return contador_palavras.most_common(n)