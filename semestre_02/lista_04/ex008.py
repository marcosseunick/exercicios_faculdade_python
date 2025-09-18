import heapq

class GerenciadorTarefas:

    def __init__(self):
     
        self._tarefas = []

    def adicionar(self, prioridade: int, descricao: str):

        tarefa = (prioridade, descricao)
      
        heapq.heappush(self._tarefas, tarefa)
        print(f"Adicionada: '{descricao}' com prioridade {prioridade}.")

    def executar_proxima(self) -> str:

        if not self._tarefas:
            return "Nenhuma tarefa para executar."
  
        prioridade, descricao = heapq.heappop(self._tarefas)
        return descricao

    def listar(self):
  
        if not self._tarefas:
            print("Não há tarefas pendentes.")
            return

        print("\n--- Tarefas Pendentes (ordenadas por prioridade) ---")
  
        for prioridade, descricao in sorted(self._tarefas):
            print(f"  Prioridade {prioridade}: {descricao}")
        print("--------------------------------------------------")