def contagem_regressiva(n):

    if n == 0:
        print("0")
        print("Decolar!")
        return

    #
    else:
        print(f"{n}, ", end="") 
        contagem_regressiva(n - 1)
