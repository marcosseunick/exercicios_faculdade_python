def fatorial_visual(n):
  
    if n == 1:
        return 1, "1"
    
    valor_anterior, texto_anterior = fatorial_visual(n - 1)
    
    valor_atual = n * valor_anterior
    texto_atual = f"{n} * {texto_anterior}"
    
    return valor_atual, texto_atual

def mostrar_fatorial(n):
    resultado, expressao = fatorial_visual(n)
    print(f"{expressao} = {resultado}")

