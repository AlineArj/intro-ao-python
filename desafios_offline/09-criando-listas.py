# Exercise: Use lists to store planet names

# As listas permitem que você armazene vários valores em uma única variável. Neste caderno, você criará um projeto para exibir informações sobre os planetas.

# Primeiro, crie uma variável chamada planetas. Adicione os oito planetas (sem Plutão) à lista. 
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']

# Termine usando print para exibir a lista de planetas.
print('Os planetas do sistema solar são: ')

for planeta in planetas:
    print(planeta)

# Display the number of planets
# Em seguida, exiba o número total de planetas usando len e print.
print()
print(f'Existem {len(planetas)} planetas no Sistema Solar!')

# Add a planet to the list
# Finally, add Pluto to the list that you created. Then display both the number of planets and the last planet in the list.
planetas.append('Plutão')
print()
print(f'Antigamente se considerava  {len(planetas)} planetas no Sistema Solar')
print(f'Porém, {planetas[-1]} foi rebaixado a planeta anão e retirado dessa contagem.')
