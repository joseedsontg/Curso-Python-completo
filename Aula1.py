#Seção 1: Lógica de Programação
#Código simples de soma com algumas maneiras diferentes de ser feito

#começando com o jeito mais básico
a = 1
b = 2
print(a + b)

#agora com uma variável recebendo a soma
a = 1
b = 2
soma = a + b
print(soma)

#agora com modularização
def soma(A, B):
    som = A + B
    print(som)

a = 1
b = 1
soma(a, b)