# Armazene cada contato em uma linha no formato nome;telefone1,telefone2,.... 
# Implemente operações: ADD, DEL, FIND, LIST. Grave e leia do mesmo arquivo.
# Entrada (exemplo): ADD Ana;11-9999-1234, ADD Bia;11-8888-0000, FIND Ana
# Saída (exemplo): Ana;11-9999-1234.
contatos_em_memoria = {}

NOME_ARQUIVO = "semestre_02\lista_05\ex001\contatos.txt"

try:
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as agenda:
        for linha in agenda:
            linha_limpa = linha.strip()
            if linha_limpa:
                partes = linha_limpa.split(";")
                if len(partes) == 2:
                    chave = partes[0]
                    valor = partes[1]
                    contatos_em_memoria[chave] = valor
                else:
                    print(f"Aviso: Linha mal formatada no arquivo: '{linha_limpa}'")

except FileNotFoundError:
    print(f"Arquivo '{NOME_ARQUIVO}' não encontrado. Começando com a agenda vazia.")

print("\n--- Agenda Pronta ---")

def salvar_no_arquivo(dicionario_para_salvar, NOME_ARQUIVO):
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            for chave, valor in dicionario_para_salvar.items():
                arquivo.write(f"{chave};{valor}\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar o aquivo {NOME_ARQUIVO} : {e}")
        return False

while True:
    print("1. ADD")
    print("2. DEL")
    print("3. FIND")
    print("4. LIST")
    comando = input("Digite o número do comando")

    if comando == "1":
        print("\n--- Adicionar Novo Contato ---")

        entrada_usuario = input("Digite o contato (formato: nome;telefone1,telefone2,...): ").strip()
        
        if not entrada_usuario or ";" not in entrada_usuario:
            print("Erro: Formato inválido. Use 'nome;telefones'.")
            continue

        try:
            nome, telefones = entrada_usuario.split(";", 1)
            nome_limpo = nome.strip()
            telefones_limpos = telefones.strip()
            if not nome_limpo or not telefones_limpos:
                print("Erro: O nome e os telefones não podem estar vazios.")
                continue
            if nome_limpo in contatos_em_memoria:
                print(f"Erro: O contato '{nome_limpo}' já existe na agenda.")
            else:
                contatos_em_memoria[nome_limpo] = telefones_limpos
                sucesso = salvar_no_arquivo(contatos_em_memoria, NOME_ARQUIVO)
                if sucesso:
                    print(f"Sucesso: Contato '{nome_limpo}' adicionado!")
                else:
                    print(f"Erro: Contato '{nome_limpo}' foi adicionado à memória, mas FALHOU ao salvar no arquivo.")
        except Exception as e:
            print(f"Erro inesperado ao processar a entrada: {e}")


    elif comando == "2":
        print("\n--- Deletar Contato ---")
        
        nome_para_deletar = input("Digite o nome do contato que deseja deletar: ")
        nome_limpo = nome_para_deletar.strip()

        if not nome_limpo:
            print("Erro: O nome não pode ser vazio.")
            continue 

        if nome_limpo in contatos_em_memoria:
            try:
                del contatos_em_memoria[nome_limpo]
                
                sucesso = salvar_no_arquivo(contatos_em_memoria, NOME_ARQUIVO)

                if sucesso:
                    print(f"Sucesso: Contato '{nome_limpo}' foi deletado.")
                else:
                    print(f"Erro: Contato '{nome_limpo}' deletado da memória, mas FALHOU ao salvar a remoção no arquivo.")
            
            except Exception as e:
                print(f"Erro inesperado ao tentar deletar '{nome_limpo}': {e}")
        else:
            print(f"Erro: O contato '{nome_limpo}' não foi encontrado na agenda.")
            

    elif comando == "3":
        print("\n--- Procurar Contato ---")
        
        nome_para_procurar = input("Digite o nome do contato que deseja procurar: ")
        
        nome_limpo = nome_para_procurar.strip()

        if not nome_limpo:
            print("Erro: O nome não pode ser vazio.")
            continue 

        if nome_limpo in contatos_em_memoria:
         
            telefones = contatos_em_memoria[nome_limpo]
            
            print(f"Contato encontrado: {nome_limpo};{telefones}")
        else:
            print(f"Erro: O contato '{nome_limpo}' não foi encontrado na agenda.")
            


    elif comando == "4":
        print("\n--- Lista de Contatos ---")
        
        
        if contatos_em_memoria:
            for nome, telefones in contatos_em_memoria.items():
                    print(f"{nome};{telefones}")
        else:
            print("A agenda de contatos está vazia.")


    elif comando.lower() == "sair": 
        print("Finalizando o programa...")
        break 

 
    else:
        print("Erro: Comando inválido. Digite 1, 2, 3, 4 ou 'sair'.")


print("Programa finalizado.")