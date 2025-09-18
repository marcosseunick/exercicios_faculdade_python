agenda = {}

def adicionar(nome, telefones):
    agenda[nome] = telefones

def remover(nome):
    if nome in agenda:
        del agenda[nome]
        return True
    return False

def buscar(termo):
    termo = termo.lower()
    return {nome: tels for nome, tels in agenda.items() if termo in nome.lower()}


adicionar("Ana Paula", ["11-9999-1234"])
adicionar("Carlos Silva", ["11-8888-4321"])
print(buscar("ana"))  
remover("Carlos Silva")
print(agenda)