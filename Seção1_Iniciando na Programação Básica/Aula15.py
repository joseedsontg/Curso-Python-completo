#Seção 1: Lógica de Programação
#Esta aula é uma introdução aos blocos de códigos condicionais em Python
#Esses blocos permitem que o programa tome decisões baseadas em condições específicas   
#Vamos explorar as estruturas condicionais if, elif e else 
# if / elif / else
# se/ se não se / senao 

entrada = input("Voce quer entrar ou sair?: ")

if entrada == 'entrar': #se a condição for verdadeira 
    print("Voce entrou no sistema.") #ele imprime essa mensagem
elif entrada == 'sair': #se a primeira condição for falsa, ele verifica essa
    print("Voce saiu do sistema.") #se essa for verdadeira, ele imprime essa mensagem
else: #se ambas forem falsas
    print("comando invalido! :(") #esta mensagem é imprimida