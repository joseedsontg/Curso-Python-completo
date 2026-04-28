#Seção 1: Lógica de Programação
#Esta aula será sobre inputs para coleta de dados do usuário

#geralmente prefiro atribuir o input a uma variável para facilitar o uso posterior
nome = input('Digite seu nome: ') #input sempre retorna uma string
numero = int(input('Digite um número: ')) #convertemos a string retornada para inteiro com int()
decimal = float(input('Digite um número decimal: ')) #convertemos a string retornada para float com float()

print(f"Olá, {nome}") #vai printar o nome digitado pelo usuário
print(f"O número que você digitou foi {numero}") #vai printar o número inteiro digitado pelo usuário
print(f"O número decimal que você digitou foi {decimal}") #vai printar o número decimal digitado pelo usuário

#ATENÇÃO: a função input() sempre retorna uma string
#se você precisa de um tipo específico (int, float, etc), você deve converter a string retornada