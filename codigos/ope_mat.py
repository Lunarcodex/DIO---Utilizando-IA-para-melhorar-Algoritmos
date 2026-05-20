# Vamos solicitar ao usuário como entrada dois números e depois vamos solicitar a ele qual operação deseja realizar. Vamos fazer uma calculadora com as  4 operações básicas que na subtração retorna valores absolutos.

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = float(num1) + float(num2)  
elif operacao == "-":
    resultado = abs(float(num1) - float(num2))
elif operacao == "*":
    resultado = float(num1) * float(num2)
elif operacao == "/":
    if float(num2) != 0:
        resultado = float(num1) / float(num2)
    else:
        resultado = "Erro: Divisão por zero"

print("O resultado da operação é: " + str(resultado))