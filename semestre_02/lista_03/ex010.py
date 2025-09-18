from collections import deque

def simular_fila(operacoes):
    
    fila_atendimento = deque()
    atendidos = []

    print("--- Processando Operações ---")
    for op in operacoes:
        print(f"Executando: '{op}'")
        partes = op.split()
        comando = partes[0].upper() 

        if comando == "CHEGA" and len(partes) > 1:
            nome = partes[1]
           
            fila_atendimento.append(nome)
        
        elif comando == "PRIORITARIO" and len(partes) > 1:
            nome = partes[1]
           
            fila_atendimento.appendleft(nome)

        elif comando == "ATENDE":
            if fila_atendimento:
              
                pessoa_atendida = fila_atendimento.popleft()
                atendidos.append(pessoa_atendida)
            else:
                print("Aviso: Tentativa de atender, mas a fila está vazia.")
        
        else:
            print(f"Aviso: Comando desconhecido ou mal formatado: '{op}'")
            
        print(f"  Fila atual: {list(fila_atendimento)}")

    return atendidos, list(fila_atendimento)

if __name__ == "__main__":
   
    lista_de_operacoes = [
        "CHEGA Ana",
        "CHEGA Bia",
        "PRIORITARIO João",
        "CHEGA Carlos",
        "ATENDE",
        "ATENDE",
        "PRIORITARIO Maria",
        "ATENDE"
    ]

    
    atendidos_final, na_fila_final = simular_fila(lista_de_operacoes)

    print("\n" + "="*25)
    print("--- Resultado Final ---")
    
    print(f"Atendidos: {', '.join(atendidos_final)}")
    print(f"Na fila: {', '.join(na_fila_final)}")
    print("="*25)