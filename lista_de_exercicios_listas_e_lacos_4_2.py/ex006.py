def descriptografar(mensagem, codigo):
    binario = bin(codigo)[2:]
    
    tamanho_diferenca = len(mensagem) - len(binario)
    binario_completo = ('0' * tamanho_diferenca) + binario
    
    mensagem_final = ''
    
    for i in range(len(mensagem)):
        
        if binario_completo[i] == '1':
            mensagem_final += mensagem[i]
    
  
    return mensagem_final

print(descriptografar("abcdef", 5))   
print(descriptografar("hello", 3))    
print(descriptografar("world", 1))   