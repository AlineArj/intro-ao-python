# Calculando valores

#  Nesse cenário, você calculará o número total de luas no sistema solar e o número médio de luas que um planeta tem. Você fará isso usando um objeto de dicionário.

# Comece criando uma variável chamada planet_moons como um dicionário com as seguintes chaves/valores:
# mercury: 0,
# venus: 0,
# earth: 1,
# mars: 2,
# jupiter: 79,
# saturn: 82,
# uranus: 27,
# neptune: 14,
# pluto: 5,
# haumea: 2,
# makemake: 1,
# eris: 1
luas_dos_planetas = {
    'Mercúrio': 0,
    'Vênus': 0,
    'Terra': 1,
    'Marte': 2,
    'Júpiter': 79,
    'Saturno': 82,
    'Urano': 27, 
    'Netuno': 14,
    'Plutão': 5,
    'Haumea': 2,
    'Makemake': 1,
    'Eris': 1
    }

# Obtenha uma lista de luas e número de planetas
# Os dicionários Python permitem que você recupere todos os valores e chaves usando os métodos values e keys, respectivamente. Cada método retorna uma lista contendo os dados, que podem ser usados como uma lista regular do Python. Você pode determinar o número de itens usando len e iterar por meio dele usando loops for. No dicionário que você criou, os nomes dos planetas são as chaves e o número de luas são os valores.
# Comece recuperando uma lista com o número de luas e armazene isso em uma variável chamada luas. Em seguida, obtenha o número total de planetas e armazene esse valor em uma variável chamada total_planets.
luas = 0

for lua in luas_dos_planetas.values():
    luas += lua
print(f'Existe {luas} luas no Sistema Solar!')

planetas = []
for planeta in luas_dos_planetas.keys():
    planetas.append(planeta)
print(f'Existe {len(planetas)} no Sistema Solar.')
print(f'São separados em três categorias: Os planetas rochos {planetas[:4]}, os gigantes gasosos {planetas[4:8]} e os planetas anões {planetas[8:]}')

# Determine o número médio de luas
print(f'Os planetas do Sistema Solar contém em média {luas / len(planetas):.2f} luas')
