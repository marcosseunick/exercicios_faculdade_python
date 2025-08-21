#           3. Faça um algoritmo que receba uma frase converta cada palavra em hashtags para redes sociais, sendo que:
#           a. Deve começar com uma hashtag (#).
#           b. Todas as palavras devem ter a primeira letra maiúscula.
#           c. Apenas palavras a partir de 05 caracteres
#           Por exemplo, se a entrada for a frase: a mancha verde é o poder, a saída deve ser: #Mancha #Verde #Poder


frase = "O palme vai jogar hoje"

palavras = frase.split(" ")


hashtag1 = ""
indice = 0
if len(palavras[indice]) >= 5:
    hashtag1 = f"#{palavras[indice].capitalize()}"

hashtag2 = ""
indice = 1
if len(palavras[indice]) >= 5:
    hashtag1 = f"#{palavras[indice].capitalize()}"

hashtag3 = ""
indice = 2
if len(palavras[indice]) >= 5:
    hashtag1 = f"#{palavras[indice].capitalize()}"

hashtag4 = ""
indice = 3
if len(palavras[indice]) >= 5:
    hashtag1 = f"#{palavras[indice].capitalize()}"

hashtag5 = ""
indice = 4
if len(palavras[indice]) >= 5:
    hashtag1 = f"#{palavras[indice].capitalize()}"

print(hashtag1, hashtag2, hashtag3, hashtag4, hashtag5)
