# 1 - Solicite ao usuário que insira seu nome e imprima uma mensagem de saudação.

nome= str(input("Qual é o seu nome? "))
print("Seja bem vindo, ", nome)

# 2 - Peça dois números ao usuário, some-os e imprima o resultado.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
print("A soma de", n1, "e", n2, "é igual a", s)

# 3 - Solicite a idade do usuário e imprima uma mensagem indicando se é maior de idade.

idade = int(input("Quantos anos você tem? "))
if idade >= 18:
  print("Você é maior de idade")
else:
  print("Você não é maior de idade")

# 4 - Peça o raio de um círculo e calcule sua área. Em seguida, imprima o resultado.

r = float(input("Digite o raio do círculo: "))
a = 3.14 * (r**2)
print("A área do circulo em cm é: ", a) 

# 5 - Solicite um número e imprima sua raiz quadrada

import math
numero = float(input("Digite um número: "))
raiz_quadrada = math.sqrt(numero)
print("A raiz quadrada de", numero, "é", raiz_quadrada)

# 6 - Peça ao usuário para inserir dois números e imprima o resultado da multiplicação entre eles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
m = n1 * n2
print("A multiplicação entre", n1, "e", n2, "é igual a", m)

# 7. Solicite a altura e o peso do usuário. Calcule o IMC (Índice de Massa Corporal) e imprima o resultado.

peso = float(input("Digite seu peso em quilos (utilize ponto ao invés de vírgula): "))
altura = float(input("Digite sua altura em metros: (utilize ponto ao invés de vírgula) "))
imc = peso/altura**2
print("O seu IMC é de", imc)

# 8. Peça ao usuário para digitar um número e imprima se é positivo ou negativo.

numero = int(input("Digite um número: "))
if numero < 0:
  print("Esse número é negativo")
else:
  print("Esse número é positivo")

# 9. Solicite um valor em reais e imprima o equivalente em dólares (considere a cotação fixa).

real = float(input("Digite o Valor que deseja converter (utilize ponto ao invés de vírgula): R$"))
dolar = real * 5.81
print(real, "em dólar é ", dolar)

# 10. Peça dois números ao usuário e imprima o resultado da divisão do primeiro pelo segundo.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
d = n1 / n2
print("A divisão entre", n1, "e", n2, "é igual a", d)

# 11. Solicite um número inteiro e imprima se é par ou ímpar.

inteiro = int(input("Digite um número: "))
if inteiro % 2 == 0:
  print("O número digitado é par")
else:
  print("O número digitado é impar")

# 12. Peça ao usuário para digitar sua cidade e imprima a mensagem "Bem-vindo(a) à cidade de [cidade]".

cidade = str(input("Em que cidade você está? "))
print("Bem-vindo(a) à cidade de, ",cidade)

# 13. Solicite o valor do lado de um quadrado e imprima sua área.

l = float(input("Digite o tamanho de um lado do quadrado: "))
a = l * l 
print("A área do quadrado é: ", a)

#14. Peça a temperatura em graus Celsius e imprima a equivalente em Fahrenheit.

celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (celsius * 1.8)/32
print("A temperatura em °F é ", fahrenheit)

# 15. Solicite dois números e imprima o resultado da potência do primeiro pelo segundo.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
potencia = n1**n2
print("O resultado da potência entre", n1, "e", n2, "é", potencia)