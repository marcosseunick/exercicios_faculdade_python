def coelhos_fibonacci(mes):

    if mes <= 2:
        return 1
    
    
    else:
        return coelhos_fibonacci(mes - 1) + coelhos_fibonacci(mes - 2)


print(f"Pares de coelhos no mês 6: {coelhos_fibonacci(6)}")