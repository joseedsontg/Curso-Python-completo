#Seção 1: Lógica de Programação
#Esta aula é sobre o operador lógico OR
"""
Se houver algução verdadeira
ele avalia toda a expressão como verdadeira
"""

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_correta = "123456"

if (entrada == "E" or entrada == "e") and senha_digitada == senha_correta:#o parenteses vai ajudar a evitar ambiguidade nos dois casos
    print("Entrou no sistema")
elif (entrada == "S" or entrada == "s") and senha_digitada != senha_correta:
    print("Saiu do sistema")