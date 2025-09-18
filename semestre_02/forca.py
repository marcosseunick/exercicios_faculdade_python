def forca(secreta: str, tentativas: list[str]) -> None:
    MAX_ERROS = 6
    erros = 0
    acertos = "_" * len(secreta)

    for letra in tentativas:
        print()
        posicoes = posicoes_da_letra(secreta, letra)
        if len(posicoes) > 0:
            acertos = substitur_letra(acertos, posicoes, letra)
        else:
            erros += 1
    resultado = "ganhou" if erros < MAX_ERROS and acertos == secreta else "perdeu"
    print(f"{resultado}, erros = {erros}")

def posicoes_da_letra(palavra: str, letra: str) -> list[int]:
    posicoes = []
    for i in range(len(palavra)):
        if palavra[i] == letra:
            posicoes.append(i)
        return posicoes

def substitur_letra(acertos: str, posicoes: list[int], letra:str) -> str:
    resultado = []
    for i in range(len(acertos)):
        resultado.append(letra if i in posicoes else acertos[i])
    return "".join(resultado)