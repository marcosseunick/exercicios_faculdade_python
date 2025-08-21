def remover_linhas_vazias(nome_arquivo):
        nome_novo_arquivo = nome_arquivo.replace('.txt', '_limpo.txt')
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_original, \
             open(nome_novo_arquivo, 'w', encoding='utf-8') as novo_arquivo:
            
            for linha in arquivo_original:
                linha_limpa = linha.strip()
                
                if linha_limpa:
                    novo_arquivo.write(linha)
        
remover_linhas_vazias('exercicios.txt')