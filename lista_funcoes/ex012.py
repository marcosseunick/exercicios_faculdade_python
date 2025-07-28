def quadrado(base, altura):
    linha = ""
    for i in range(altura):
        if i == 0:
            linha += "* " * base + "\n"
        elif i == altura - 1:
            linha += "* " * base + "\n"
        else:
            linha += "*" + " " * ((base - 2) * 2 + 1) + "*" + "\n"
    return linha
