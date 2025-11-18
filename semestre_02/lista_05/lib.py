import csv
import json
import string
from collections import Counter

# --- Funções Utilitárias (Criação de Arquivos de Exemplo) ---

def criar_arquivos_de_exemplo():
    """Cria os arquivos de entrada necessários para os exercícios."""
    print("Criando arquivos de exemplo...")

    # Exercício 2: vendas.csv
    with open('vendas.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['data', 'produto', 'qtd', 'preco'])
        writer.writerow(['2025-03-01', 'caneta', 10, 2.50])
        writer.writerow(['2025-03-02', 'caderno', 2, 15.00])
        writer.writerow(['2025-03-02', 'caneta', 5, 2.50])
        writer.writerow(['2025-04-01', 'caderno', 1, 15.00])
        writer.writerow(['2025-04-05', 'borracha', 20, 1.00])

    # Exercício 3: app.log
    with open('app.log', 'w', encoding='utf-8') as f:
        f.write("INFO: Aplicação iniciada\n")
        f.write("DEBUG: Verificando conexão com DB\n")
        f.write("WARN: CPU em 80%\n")
        f.write("ERROR: Falha ao conectar no serviço X (Erro 1)\n")
        f.write("INFO: Usuário 'admin' logado\n")
        f.write("DEBUG: Processando requisição /home\n")
        f.write("ERROR: Timeout na API Y (Erro 2)\n")
        f.write("ERROR: Erro de permissão (Erro 3)\n")
        f.write("ERROR: NullPointerException (Erro 4)\n")
        f.write("INFO: Processo finalizado\n")
        f.write("ERROR: Falha ao gravar log (Erro 5)\n")
        f.write("ERROR: Conexão perdida (Erro 6)\n")

    # Exercício 4: livro.txt
    with open('livro.txt', 'w', encoding='utf-8') as f:
        f.write("Este é um exemplo de texto.\n")
        f.write("O texto contém palavras repetidas.\n")
        f.write("O objetivo é criar um índice invertido.\n")
        f.write("Um índice ajuda a buscar palavras.\n")

    # Exercício 5: texto.txt e stopwords.txt
    with open('texto.txt', 'w', encoding='utf-8') as f:
        f.write("Python é uma linguagem de programação. O Python é popular.\n")
        f.write("Este texto será usado para contar a frequência de palavras, sim, a frequência!")
    
    with open('stopwords.txt', 'w', encoding='utf-8') as f:
        f.write("de\n")
        f.write("a\n")
        f.write("o\n")
        f.write("que\n")
        f.write("e\n")
        f.write("é\n")
        f.write("do\n")
        f.write("da\n")
        f.write("em\n")
        f.write("um\n")
        f.write("para\n")
        f.write("com\n")
        f.write("não\n")
        f.write("uma\n")
        f.write("os\n")
        f.write("na\n")
        f.write("por\n")
        f.write("mais\n")
        f.write("as\n")
        f.write("dos\n")
        f.write("como\n")
        f.write("mas\n")
        f.write("ao\n")
        f.write("ele\n")
        f.write("das\n")
        f.write("à\n")
        f.write("seu\n")
        f.write("sua\n")
        f.write("este\n")
        f.write("será\n")
        f.write("sim\n")

    # Exercício 6: presenca.csv
    with open('presenca.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['aluno', 'data', 'presente'])
        writer.writerow(['Ana', '2025-05-10', 1])
        writer.writerow(['Bia', '2025-05-10', 1])
        writer.writerow(['Carlos', '2025-05-10', 0])
        writer.writerow(['Ana', '2025-05-11', 1])
        writer.writerow(['Bia', '2025-05-11', 0])
        writer.writerow(['Carlos', '2025-05-11', 1])
        writer.writerow(['Ana', '2025-05-12', 0])
        writer.writerow(['Bia', '2025-05-12', 1])
        writer.writerow(['Carlos', '2025-05-12', 1])

    # Exercício 7: entrada.txt
    with open('entrada.txt', 'w', encoding='utf-8') as f:
        f.write("Python é divertido.\n")
        f.write("Aprender programação é importante.\n")

    # Exercício 9: numeros.txt
    with open('numeros.txt', 'w', encoding='utf-8') as f:
        f.write("10\n")
        f.write("20\n")
        f.write("30\n")
        f.write("40\n")

    # Exercício 10: mensagem.txt
    with open('mensagem.txt', 'w', encoding='utf-8') as f:
        f.write("O aluno cometeu um erro.\n")
        f.write("Outro erro foi encontrado.\n")
        f.write("Isso é um erro grave.\n")

    print("Arquivos de exemplo criados com sucesso!\n")


# --- Soluções dos Exercícios ---

## 1. Cadastro de Contatos em TXT
# 
def exercicio_1():
    """
    Gerencia um cadastro de contatos salvo em 'contatos.txt'.
    Implementa as operações: ADD, DEL, FIND, LIST.
    """
    ARQUIVO_CONTATOS = 'contatos.txt'

    def carregar_contatos():
        """Lê o arquivo e retorna uma lista de linhas."""
        try:
            with open(ARQUIVO_CONTATOS, 'r', encoding='utf-8') as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def salvar_contatos(linhas):
        """Salva a lista de linhas de volta no arquivo."""
        with open(ARQUIVO_CONTATOS, 'w', encoding='utf-8') as f:
            f.writelines(linhas)

    def add_contato():
        """Adiciona um novo contato."""
        nome = input("Digite o nome: ")
        telefones = input("Digite os telefones (separados por vírgula): ")
        # 
        novo_contato = f"{nome};{telefones}\n"
        with open(ARQUIVO_CONTATOS, 'a', encoding='utf-8') as f:
            f.write(novo_contato)
        print(f"Contato '{nome}' adicionado.")

    def del_contato():
        """Remove um contato pelo nome."""
        nome_del = input("Digite o nome para deletar: ")
        linhas = carregar_contatos()
        novas_linhas = []
        encontrado = False
        for linha in linhas:
            if linha.strip() and not linha.startswith(nome_del + ';'):
                novas_linhas.append(linha)
            else:
                encontrado = True
        
        if encontrado:
            salvar_contatos(novas_linhas)
            print(f"Contato '{nome_del}' removido.")
        else:
            print(f"Contato '{nome_del}' não encontrado.")

    def find_contato():
        """Encontra um contato pelo nome."""
        nome_find = input("Digite o nome para buscar: ")
        linhas = carregar_contatos()
        encontrado = False
        for linha in linhas:
            if linha.strip() and linha.startswith(nome_find + ';'):
                print(f"Encontrado: {linha.strip()}") # 
                encontrado = True
                break
        if not encontrado:
            print(f"Contato '{nome_find}' não encontrado.")

    def list_contatos():
        """Lista todos os contatos."""
        linhas = carregar_contatos()
        if not linhas:
            print("Nenhum contato cadastrado.")
            return
        
        print("\n--- Lista de Contatos ---")
        for linha in linhas:
            print(linha.strip())
        print("--------------------------\n")

    # Menu principal do Exercício 1
    print("--- Exercício 1: Cadastro de Contatos ---")
    print("Este é um programa interativo.")
    while True:
        # 
        print("\nOperações: ADD, DEL, FIND, LIST, SAIR")
        cmd = input("Digite o comando: ").upper()
        
        if cmd == 'ADD':
            add_contato()
        elif cmd == 'DEL':
            del_contato()
        elif cmd == 'FIND':
            find_contato()
        elif cmd == 'LIST':
            list_contatos()
        elif cmd == 'SAIR':
            print("Saindo do cadastro.")
            break
        else:
            print("Comando inválido.")

## 2. Relatório de Vendas (CSV)
# 
def exercicio_2():
    """
    Lê 'vendas.csv' e gera 'relatorio.txt' com faturamento total,
    por produto e por mês.
    """
    # 
    faturamento_total = 0
    faturamento_produto = {}
    faturamento_mes = {}

    ARQUIVO_ENTRADA = 'vendas.csv'
    ARQUIVO_SAIDA = 'relatorio.txt' # 

    try:
        with open(ARQUIVO_ENTRADA, 'r', encoding='utf-8') as f:
            leitor_csv = csv.reader(f)
            next(leitor_csv) # Pula o cabeçalho

            for linha in leitor_csv:
                # 
                data, produto, qtd_str, preco_str = linha
                qtd = int(qtd_str)
                preco = float(preco_str)
                
                faturamento_linha = qtd * preco
                mes_ano = data[0:7] # Formato AAAA-MM 
                
                # 1. Faturamento total
                faturamento_total += faturamento_linha
                
                # 2. Faturamento por produto
                faturamento_produto[produto] = faturamento_produto.get(produto, 0) + faturamento_linha
                
                # 3. Faturamento por mês
                faturamento_mes[mes_ano] = faturamento_mes.get(mes_ano, 0) + faturamento_linha

        # Gera o relatorio.txt
        with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as f:
            f.write("--- Relatório de Vendas ---\n\n")
            # 
            f.write(f"Faturamento Total: R$ {faturamento_total:.2f}\n")
            f.write("\n--- Faturamento por Produto ---\n")
            for produto, total in faturamento_produto.items():
                f.write(f"{produto}: R$ {total:.2f}\n")
            
            f.write("\n--- Faturamento por Mês (AAAA-MM) ---\n")
            for mes, total in sorted(faturamento_mes.items()):
                f.write(f"{mes}: R$ {total:.2f}\n")

        print(f"Exercício 2: 'relatorio.txt' gerado com sucesso.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_ENTRADA}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

## 3. Leitura de Log e Contagem de Severidades
# 
def exercicio_3():
    """
    Lê 'app.log', conta ocorrências por nível (INFO, WARN, ERROR, DEBUG)
    e lista as 5 últimas mensagens ERROR.
    """
    # 
    niveis = {'INFO': 0, 'WARN': 0, 'ERROR': 0, 'DEBUG': 0}
    mensagens_error = []
    ARQUIVO_LOG = 'app.log'

    try:
        with open(ARQUIVO_LOG, 'r', encoding='utf-8') as f:
            for linha in f:
                linha_strip = linha.strip()
                if not linha_strip:
                    continue
                
                # Divide a linha no primeiro ':' para pegar a severidade
                partes = linha_strip.split(':', 1)
                nivel = partes[0]
                
                if nivel in niveis:
                    niveis[nivel] += 1
                    if nivel == 'ERROR':
                        # Salva a mensagem (parte[1])
                        mensagens_error.append(partes[1].strip() if len(partes) > 1 else "Sem mensagem")

        print("--- Exercício 3: Contagem de Logs ---")
        # 
        print("Contagem por nível:")
        for nivel, contagem in niveis.items():
            print(f"{nivel}: {contagem}")
        
        print("\nÚltimas 5 mensagens de ERROR:")
        # 
        ultimos_5_erros = mensagens_error[-5:] # Pega os 5 últimos
        if not ultimos_5_erros:
            print("Nenhuma mensagem de ERROR encontrada.")
        else:
            for msg in ultimos_5_erros:
                print(f"- {msg}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_LOG}' não encontrado.")

## 4. Busca e Índice Invertido (TXT)
# 
def exercicio_4():
    """
    Cria um índice invertido (palavra: [linhas]) de 'livro.txt'
    e salva o índice em 'indice.json'.
    """
    # 
    indice_invertido = {}
    ARQUIVO_TEXTO = 'livro.txt'
    ARQUIVO_JSON = 'indice.json' # 

    # Tabela de tradução para remover pontuação
    translator = str.maketrans('', '', string.punctuation)

    try:
        with open(ARQUIVO_TEXTO, 'r', encoding='utf-8') as f:
            # Usamos enumerate(..., start=1) para contar linhas a partir do 1
            for num_linha, linha in enumerate(f, start=1):
                # Limpeza: minúsculas, remove pontuação
                linha_limpa = linha.lower().translate(translator)
                palavras = linha_limpa.split()
                
                for palavra in palavras:
                    if palavra not in indice_invertido:
                        indice_invertido[palavra] = []
                    
                    # Adiciona o número da linha apenas se ainda não estiver lá
                    if num_linha not in indice_invertido[palavra]:
                        indice_invertido[palavra].append(num_linha)

        # Salva o índice em JSON
        # 
        with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f_json:
            json.dump(indice_invertido, f_json, indent=4, ensure_ascii=False)
        
        print(f"--- Exercício 4: Índice Invertido ---")
        print(f"Índice invertido salvo em '{ARQUIVO_JSON}'.")

        # Exemplo de consulta 
        print("\nExemplo de consulta no índice:")
        if 'texto' in indice_invertido:
             # (exemplo adaptado)
            print(f"'texto' aparece nas linhas: {indice_invertido['texto']}")
        if 'índice' in indice_invertido:
            print(f"'índice' aparece nas linhas: {indice_invertido['índice']}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_TEXTO}' não encontrado.")

## 5. Frequência de Palavras com Stopwords
# 
def exercicio_5():
    """
    Lê 'texto.txt', remove stopwords de 'stopwords.txt',
    e gera 'top_20.csv' com as palavras mais frequentes.
    """
    # 
    ARQUIVO_TEXTO = 'texto.txt'
    ARQUIVO_STOPWORDS = 'stopwords.txt'
    ARQUIVO_SAIDA = 'top_20.csv' # 
    
    try:
        # 1. Carregar stopwords
        with open(ARQUIVO_STOPWORDS, 'r', encoding='utf-8') as f:
            # Usamos um set() para busca rápida
            stopwords = set(linha.strip() for linha in f)
            
        # 2. Ler e processar o texto principal
        with open(ARQUIVO_TEXTO, 'r', encoding='utf-8') as f:
            texto_completo = f.read()
            
            # 3. Limpar (pontuação e minúsculas)
            # 
            translator = str.maketrans('', '', string.punctuation)
            texto_limpo = texto_completo.lower().translate(translator)
            
            palavras = texto_limpo.split()
            
            # 4. Filtrar stopwords
            palavras_filtradas = [p for p in palavras if p not in stopwords and p]
            
            # 5. Contar frequência
            contagem = Counter(palavras_filtradas)
            
            # 6. Obter as 20 mais comuns
            top_20 = contagem.most_common(20)
            
            # 7. Salvar em top_20.csv
            with open(ARQUIVO_SAIDA, 'w', newline='', encoding='utf-8') as f_csv:
                writer = csv.writer(f_csv)
                writer.writerow(['palavra', 'contagem']) # Cabeçalho 
                writer.writerows(top_20)
                
            print("--- Exercício 5: Frequência de Palavras ---")
            print(f"'{ARQUIVO_SAIDA}' gerado com sucesso.")
            print("Top 5 palavras:")
            for item in top_20[:5]:
                print(f"- {item[0]}: {item[1]}")

    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e.filename}")

## 6. Controle de Presença (CSV)
# 
def exercicio_6():
    """
    Lê 'presenca.csv' e gera relatório de faltas e
    percentual de presença por aluno.
    """
    # 
    ARQUIVO_PRESENCA = 'presenca.csv'
    estatisticas_alunos = {} # Dicionário para guardar {'aluno': {'presente': 0, 'total': 0}}

    try:
        with open(ARQUIVO_PRESENCA, 'r', encoding='utf-8') as f:
            leitor_csv = csv.reader(f)
            next(leitor_csv) # Pula cabeçalho
            
            for linha in leitor_csv:
                # 
                aluno, data, presente_str = linha
                presente = int(presente_str) # 0 ou 1
                
                # Inicializa o aluno se for a primeira vez
                if aluno not in estatisticas_alunos:
                    estatisticas_alunos[aluno] = {'presente': 0, 'total': 0}
                
                # Atualiza estatísticas
                estatisticas_alunos[aluno]['total'] += 1
                if presente == 1:
                    estatisticas_alunos[aluno]['presente'] += 1

        print("--- Exercício 6: Controle de Presença ---")
        if not estatisticas_alunos:
            print("Nenhum dado de presença encontrado.")
            return

        # 
        print("Relatório de Presença por Aluno:")
        for aluno, dados in sorted(estatisticas_alunos.items()):
            total_aulas = dados['total']
            aulas_presente = dados['presente']
            faltas = total_aulas - aulas_presente
            
            if total_aulas > 0:
                percentual_presenca = (aulas_presente / total_aulas) * 100
            else:
                percentual_presenca = 0
            
            # 
            print(f"- {aluno}: {percentual_presenca:.1f}% presença (faltas={faltas}/{total_aulas})")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_PRESENCA}' não encontrado.")

## 7. Programa que copia conteúdo de um arquivo para outro
# 
def exercicio_7():
    """
    Copia o conteúdo de 'entrada.txt' para 'saida.txt'.
    """
    # 
    ARQUIVO_ENTRADA = 'entrada.txt'
    ARQUIVO_SAIDA = 'saida.txt'

    print("--- Exercício 7: Copiar Arquivo ---")
    try:
        with open(ARQUIVO_ENTRADA, 'r', encoding='utf-8') as f_in:
            conteudo = f_in.read() # Lê todo o conteúdo
        
        with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as f_out:
            f_out.write(conteudo) # Escreve o conteúdo no novo arquivo
            
        print(f"Arquivo '{ARQUIVO_ENTRADA}' copiado para '{ARQUIVO_SAIDA}'.")
        # 
        print("\nConteúdo de 'saida.txt':")
        print(conteudo)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_ENTRADA}' não encontrado.")

## 8. Programa que insere texto ao final de um arquivo
# 
def exercicio_8():
    """
    Pede uma frase ao usuário e a insere no final de 'anotacoes.txt'.
    """
    # 
    ARQUIVO_ANOTACOES = 'anotacoes.txt'
    
    # Criando um conteúdo inicial (apenas para o exemplo ficar igual ao PDF)
    if 'anotacoes.txt' not in [f.name for f in __import__('os').listdir('.')]:
        with open(ARQUIVO_ANOTACOES, 'w', encoding='utf-8') as f:
            f.write("Conteúdo já existente no arquivo.\n") # 

    print("--- Exercício 8: Adicionar Anotação ---")
    # (Exemplo de entrada)
    frase = input("Digite a frase que deseja adicionar: ")
    
    # 
    # Usamos o modo 'a' (append) para adicionar ao final
    try:
        with open(ARQUIVO_ANOTACOES, 'a', encoding='utf-8') as f:
            f.write(frase + "\n") # Adiciona a frase e uma nova linha
        
        print(f"Frase adicionada com sucesso em '{ARQUIVO_ANOTACOES}'.")
        
        # Mostra o conteúdo atualizado
        print(f"\nConteúdo atual de '{ARQUIVO_ANOTACOES}':")
        with open(ARQUIVO_ANOTACOES, 'r', encoding='utf-8') as f:
            print(f.read())

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

## 9. Programa que lê números de um arquivo e calcula a média
# 
def exercicio_9():
    """
    Lê números (um por linha) de 'numeros.txt' e calcula a média.
    """
    # 
    ARQUIVO_NUMEROS = 'numeros.txt'
    numeros = []
    
    print("--- Exercício 9: Média de Números ---")
    try:
        with open(ARQUIVO_NUMEROS, 'r', encoding='utf-8') as f:
            for linha in f:
                linha_limpa = linha.strip()
                if linha_limpa: # Ignora linhas em branco
                    try:
                        numeros.append(int(linha_limpa))
                    except ValueError:
                        print(f"Ignorando linha não numérica: '{linha_limpa}'")
        
        if numeros:
            media = sum(numeros) / len(numeros)
            # (O exemplo mostra 25.0, então formatamos como float)
            print(f"Os números lidos foram: {numeros}")
            print(f"A média dos números é {media:.1f}")
        else:
            print("Nenhum número encontrado no arquivo.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_NUMEROS}' não encontrado.")

## 10. Programa que substitui palavras em um arquivo
# 
def exercicio_10():
    """
    Lê 'mensagem.txt', substitui "erro" por "acerto" e
    salva em 'mensagem_corrigida.txt'.
    """
    # 
    ARQUIVO_ENTRADA = 'mensagem.txt'
    ARQUIVO_SAIDA = 'mensagem_corrigida.txt'
    PALAVRA_ANTIGA = "erro"
    PALAVRA_NOVA = "acerto"

    print("--- Exercício 10: Substituir Palavras ---")
    try:
        with open(ARQUIVO_ENTRADA, 'r', encoding='utf-8') as f_in:
            conteudo_original = f_in.read()
            # (Exemplo de entrada)
            print(f"Conteúdo Original ({ARQUIVO_ENTRADA}):\n{conteudo_original}")
        
        # Realiza a substituição
        conteudo_corrigido = conteudo_original.replace(PALAVRA_ANTIGA, PALAVRA_NOVA)
        
        with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as f_out:
            f_out.write(conteudo_corrigido)
            
        print(f"Arquivo corrigido salvo em '{ARQUIVO_SAIDA}'.")
        # (Exemplo de saída)
        print(f"\nConteúdo Corrigido ({ARQUIVO_SAIDA}):\n{conteudo_corrigido}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_ENTRADA}' não encontrado.")




if __name__ == "__main__":

    criar_arquivos_de_exemplo()

    print("\n--- Executando todos os exercícios (não interativos) ---")
    exercicio_2()
    print("-" * 20)
    exercicio_3()
    print("-" * 20)
    exercicio_4()
    print("-" * 20)
    exercicio_5()
    print("-" * 20)
    exercicio_6()
    print("-" * 20)
    exercicio_7()
    print("-" * 20)
    exercicio_9()
    print("-" * 20)
    exercicio_10()
    print("\n--- Fim da execução ---")
    print("Para testar os exercícios 1 e 8, descomente-os manualmente e execute o script.")