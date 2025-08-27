# Função mostrar_altura_peso()
# Peça ao usuário sua altura e peso, depois exiba:
# Sua altura é [altura] m e seu peso é [peso] kg.

def mostrar_altura_peso():
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    
    print(f"Sua altura é {altura}m e seu peso é {peso}kg")

mostrar_altura_peso()