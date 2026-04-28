#Seção 1: Lógica de Programção
#Essa aula é um exercício para calcular o IMC(índice de massa corporal)

#sei que ainda não foi falado sobre entrada de dados do usuário mas não tem problema
nome = input("Digite o seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura ** 2) #pesquisei a fórmula para calcular

print(f"Ola {nome} seu IMC e : {imc:.2f}")

"""
Quando estiver em um código três pontos após o sinal de =
como por exemplo 'IMC = ...' isso se chama Ellipsis,
e não gera nenhum erro no código
"""