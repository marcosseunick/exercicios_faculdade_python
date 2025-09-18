# Gerador de Senhas com secrets e string
# Enunciado: Função gerar_senha(tam, maiusculas=True, digitos=True, simbolos=True) 
# que monta o alfabeto permitido e usa secrets.choice para montar senhas fortes. Garanta ao menos um de cada tipo escolhido.
# Entrada (exemplo): gerar_senha(10, True, True, False)
# Saída (exemplo): "aB9kTqLmRp".

import secrets
import string

def gerar_senha(tam, maiusculas, digitos, simbolos) -> str:

    alfabeto = string.ascii_lowercase
    tipos = []
    if maiusculas:
        alfabeto += string.ascii_uppercase
        tipos.append(string.ascii_uppercase)
    if digitos:
        alfabeto += string.digits
        tipos.append(string.digits)
    if simbolos:
        alfabeto += string.punctuation
        tipos.append(string.punctuation)

    if not tipos:
        tipos.append(string.ascii_lowercase)

    senha = [secrets.choice(t) for t in tipos]
    senha += [secrets.choice(alfabeto) for _ in range(tam - len(senha))]
    secrets.SystemRandom().shuffle(senha)
    return ''.join(senha)
print(gerar_senha(10, True, True, False))