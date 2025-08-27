# Função operacoes_booleanas()
# Receba dois valores booleanos e mostre o resultado das operações:
# and
# or
# not (em cada valor separadamente)


def operacoes_booleanas():
  
  valor_a = True
  valor_b = False

  print(f"Analisando A={valor_a} e B={valor_b}")
  print(f"A and B: {valor_a and valor_b}") 
  print(f"A or B: {valor_a or valor_b}")   
  print(f"not A: {not valor_a}")           
  print(f"not B: {not valor_b}")           

operacoes_booleanas()