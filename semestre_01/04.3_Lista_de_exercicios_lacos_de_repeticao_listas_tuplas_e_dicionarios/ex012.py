#Peça uma senha ao usuário até que ele digite a senha correta.
senha = "A25D3M9F"
while True:
        usuario = str(input("Digite a senha: "))
        if usuario == senha:
            print("Acesso Liberado")
            break
        else:
            print("Incorreto")