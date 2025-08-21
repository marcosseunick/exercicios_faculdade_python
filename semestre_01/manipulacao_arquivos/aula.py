# arquivo = open("texto.txt", "r")
# msg = arquivo.read()
# arquivo.close()

# print(msg)

# with open("texto.txt", "r") as arq:
#     leitura = arq.read()
# print("---------")
# print(leitura)

#Fazer arquivo novo ou sobrescrever:
# msg = "A nota de matemática foi 9.0"
# with open("texo.txt", "w") as arquivo:
#      arquivo.write(msg) 

#adicionando no arquivo:

with open("texto.txt") as arq:
    conteudo = arq.read()

conteudo += "\nA nota de História foi 9.7"

with open("texto.txt", "w") as arq:
    arq.write(conteudo)