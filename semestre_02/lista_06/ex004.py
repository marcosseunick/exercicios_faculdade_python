def contar_arquivos(item):
    contador = 0
    

    if isinstance(item, list):
        for sub_item in item:
            contador += contar_arquivos(sub_item) 

    
    elif isinstance(item, str):
        contador = 1
        
    return contador

# Teste
sistema = ["a.txt", ["b.txt", "c.txt"]]
print(f"Total de arquivos: {contar_arquivos(sistema)}")