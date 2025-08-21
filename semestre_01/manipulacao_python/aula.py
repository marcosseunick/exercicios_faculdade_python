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
#     arquivo.write(msg) 

#adicionando no arquivo:
caminho = "\Users\marcos.vferreira\Documents\GitHub\exercicios_faculdade_python\manipulacao_python\texo.txt"
with open(caminho) as arq:
    conteudo = arq.read()

conteudo += "\nA nota de História foi 9.7"

with open("texto.txt", "w") as arq:
    arq.write(conteudo)