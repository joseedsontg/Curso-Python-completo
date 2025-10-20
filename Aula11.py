#Seção 1: Lógica de Programação
#Essa aula será sobre a precedência dos operadores aritmeticos em python
# precedência = ordem em que são executados antes de outros

"""
1. (n + n) ---> parenteses
2. ** ---> potenciação
3. *, /, //, % ---> multiplicação, divisões e resto
4. +, -, ---> soma e subtração 
"""

#aqui a conta deveria ser ((1 + 1) ^ (5 + 5)) = 2^10 = 1024
conta_errada = 1 + 1 ** 5 + 5 
print(conta_errada) #resultado errado vai ser 7

#eu pessoalmente prefiro deixar a ordem explícita usando parenteses 
conta_certa = ((1 + 1) ** (5 + 5))
print(conta_certa) #resultado certo deve ser 1024 = 2^10