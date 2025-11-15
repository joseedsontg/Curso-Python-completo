#Seção 1: Lógica de Programação
#Essa aula é sobre a formatação de strings com o método .format()

a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f}'#pode colocar índices dentro das chaves {} indicando a ordem dos valores
formato = string.format(a, b, c)
#cada chave {} é substituída pelos valores passados no método format
#na ordem em que foram passados

print(formato)