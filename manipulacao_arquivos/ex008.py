def buscar_palavra(nome_arquivo, palavra):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            ocorrencias = conteudo.lower().count(palavra.lower())          
            return ocorrencias

