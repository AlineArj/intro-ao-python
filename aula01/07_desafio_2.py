# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

cidade = str(input('Digite a sua cidade: '))
estado = str(input('Digite o seu estado: '))
# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.
print(f'A cidade do usuário é {cidade.upper()}')

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
print('O estado do usuário é ' + str(estado.upper()))
