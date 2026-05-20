# Vamos solicitar como entrada de uma string e um número e depois vamos realizar uma operação simples e
# vamos repetir a string o número de vezes que o usuário digitou e vamos adicionar um espaço entre as repetições

texto = input("Digite um texto: ")
numero = int(input("Digite um número: "))
texto_repetido = (texto + " ") * numero
print("O texto repetido é: " + texto_repetido)