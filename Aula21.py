#Seção 1: Lógica de Programação
"""
Interpolação básica de strings em Python
s -> string
d e i -> int
f e F -> float
x e X -> hexadecimal (ABCDEF0123456789)
usando o operador % para formatar a string, 
onde %s é substituído por uma string e %f é substituído
 por um número de ponto flutuante.
"""

nome = 'Maria'
preco = 49.99
variavel = '%s, o preço é R$%.2f' % (nome, preco)# Interpolação básica usando o operador %
print(variavel)
print('O hexadecimal de %d, é %x' % (15, 15))