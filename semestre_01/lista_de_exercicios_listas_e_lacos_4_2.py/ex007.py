terreno = [
    'XOOXO',
    'XOOXO',
    'OOOXO',
    'XXOXO',
    'OXOOO'
]
perimetro = []
comprimento = len(terreno)
for i in range(comprimento):
    largura = len(terreno[1])
    for j in range(largura):
        if terreno[i][j] == 'X':
            valor = 4
           
            if j < largura - 1 and terreno[i][j + 1] == 'X':
                valor -= 1
           
            if j > 0 and terreno[i][j - 1] == 'X':
                valor -= 1
           
            if i < comprimento - 1 and terreno[i + 1][j] == 'X':
                valor -= 1
           
            if i > 0 and terreno[i - 1][j] == 'X':
                valor -= 1
           
            perimetro.append(valor)

print(sum(perimetro))