#   CÁLCULADORA EM PYTHON

#   RAs: 
#   HENRIQUE YUI ODA - 22.01162-5
#   LEONARDO RIBEIRO DE ALMEIDA - 22.01552-3
#   LUIGI KENZO ISHII - 22.01390-3

#   Funções da calculadora:
def adicao(x , y):
    return x + y

def subtracao(x , y):
    return  x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

print("Escolha a operação desejada: ")
print("+ = Adição")
print("- = Subtração")
print("* = Multiplicação")
print("/ = Divisão")

operacao = str(input("Insira a operação de10sejada (+, -, * ou /): "))

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if operacao == "+":
    print(numero_1, "+", numero_2, "=", adicao(numero_1, numero_2))

elif operacao == "-":
    print(numero_1, "-", numero_2, "=", subtracao(numero_1, numero_2))

elif operacao == "*":
    print(numero_1, "*", numero_2, "=", multiplicacao(numero_1, numero_2))

elif operacao == "/":
    print(numero_1, "/", numero_2, "=", divisao(numero_1, numero_2))

else:
    print("Operação inválida (+, -, * ou /)")