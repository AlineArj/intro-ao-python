# Use slices to retrieve portions of a list

# Você pode precisar trabalhar diferentes seções de uma lista. Neste notebook, você criará um projeto para exibir planetas mais próximos e mais distantes do sol do que um planeta que o usuário entrar.

# Primeiro, crie uma variável chamada planetas. Adicione os oito planetas (sem Plutão) à lista. 
from operator import index


planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']

# Solicitar ao usuário o planeta de referência
# Em seguida, você adicionará o código para solicitar ao usuário o nome de um planeta. Você fará isso usando input. Como as strings diferenciam maiúsculas de minúsculas em Python, peça ao usuário para usar uma letra maiúscula para iniciar o nome do planeta.
input_planeta = input('Digite o nome de um planeta do Sistema Solar: ')
input_planeta = input_planeta.capitalize()

# Encontre a localização do planeta selecionado
# Agora é hora de determinar quais planetas estão mais próximos do que aquele que o usuário digitou. Para fazer isso, você precisa encontrar onde o planeta está na lista. Você pode usar o método de índice para realizar esta operação. Adicione o código para encontrar o índice do planeta e armazene-o em uma variável chamada planet_index.
# Exibir planetas mais próximos do sol
# Com o índice determinado, agora você pode adicionar o código para exibir planetas mais próximos do sol do que o selecionado. Use as habilidades de fatiamento de uma lista para exibir todos os planetas até o selecionado.
# Exibir planetas ainda mais
# Você pode usar o mesmo índice para exibir planetas mais distantes do sol. No entanto, lembre-se de que o índice inicial é incluído quando você usa uma fatia. Como resultado, você terá que adicionar 1 ao valor. Adicione o código para exibir os planetas mais distantes do sol.
print()
if input_planeta in planetas:
    index_planeta = planetas.index(input_planeta)

    print(f'Os planetas anteriores a {input_planeta} são: ')
    for planeta in planetas[:index_planeta]:
        print(planeta)
    
    print()

    print(f'Os planetas posteriores a {input_planeta} são: ')
    for planeta in planetas[index_planeta + 1:]:
        print(planeta)

else:
    print(f'O planeta {input_planeta} não se encontra no Sistema Solar!')
