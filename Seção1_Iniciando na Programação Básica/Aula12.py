#Seção 1: Lógica de Programação
#Essa aula é sobre f-strings (formatação de strings), uma introdução breve

nome = 'Jose Edson'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'#coloca um f no começo da string
linha_2 = f'pesa {peso} quilos e seu imc é'#para usar variáveis dentro da string temos que colocar entra chaves {}
linha_3 = f'{imc:.2f}'#para formatar números usamos : e depois o formato desejado
#no caso .2f formata o número para float com 2 casas decimais

print(linha_1)
print(linha_2)
print(linha_3)

# Jose Edson tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987