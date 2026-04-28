#Seção 1: Lógica de Programação
#Esta aula é sobre o operador lógico AND
"""
No and todas as condições precisam ser verdadeiras
para que o resultado final seja verdadeiro.
Se um valor for considarado falso,
toda a expressão será avaliada como falsa.
"""
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_correta = "123456"

if entrada == "E" and senha_digitada == senha_correta:
    print("Entrou no sistema")
elif entrada == "S" and senha_digitada != senha_correta:
    print("Saiu do sistema")    