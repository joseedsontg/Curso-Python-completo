#Seção 1: Lógica de Programação
#Esta aula é sobre os operadores IN e NOT IN
#Usados para verificar a presença de um elemento em uma coleção 
# 0 1 2 3 ---> índices
# j o s e ---> string

nome = 'jose'
print(nome[2])#vai imprimir a letra 's', que está no índice 2
print('j' in nome) #verifica se a letra 'j' está na string 'nome' ---> retorna True
print('a' in nome) #verifica se a letra 'a' está na string 'nome' ---> retorna False
print('a' not in nome) #verifica se a letra 'a' NÃO está na string 'nome' ---> retorna True
print('ose' in nome) #verifica se a substring 'ose' está na string 'nome' ---> retorna True 
