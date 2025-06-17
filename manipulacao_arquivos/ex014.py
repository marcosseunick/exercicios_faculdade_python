import re
from collections import defaultdict

def contar_ocorrencias(nome_arquivo):
    contagem_palavras = defaultdict(int)
    with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.read()

    conteudo_limpo = re.sub(r'[^\w\s]', '', conteudo).lower()
    palavras = conteudo_limpo.split()

    for palavra in palavras:
            contagem_palavras[palavra] += 1
    return dict(contagem_palavras)