#Seção 1
"""
Formatação de String
com f-strings
s -> string
d -> int
f -> float
.<número de digitos>f
x ou X -> Hexadecimal (0123456789ABCDEF)
(Caractere)(><^)(Qauntidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
EX: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')#cria um espaço de 10 caracteres a esquerda da variável
print(f'{variavel:0<10}')#cria um espaço de 10 caracteres a direita da variável e preenche com 0

"""
Podemos usar vários símbolos pra preencher esses espaços
"""