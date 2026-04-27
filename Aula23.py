#Seção 1
"""
Fatiamento de strings usando a 
funçaõ lens()
"""

"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Ftiamento [i:f:p] [::]
i = início (de onde vai começar a printar)
f = fim (onde vai prarar de printar, sempre lebrar de usar 1 
índice a mais do que você quer)
p = passo (de quanto em quanto pula, geralmente usa-se de 1 em 1)
Obs.: a função len retorna a 
qtd de caracteres da string
"""

variavel = 'olá mundo'
print("variavel[5]")#vai printar a letra que estiver no índice 5
print("variavel[4:8]")#vai printar do índice 4 até o 7 pois ele esconde o 
#índice final, que nesse caso é o 8
print(len(variavel))#vai printar o número de caracteres da variável, que é 9
