# Exercise: Formatting strings

# Saber formatar strings é essencial quando você está apresentando informações de um programa. Existem algumas maneiras diferentes de fazer isso em Python. Neste exercício, você usa variáveis que contêm fatos importantes sobre a gravidade em várias luas e as usa para formatar e imprimir as informações.
# Este exercício é dividido em uma série de etapas. Para cada etapa, você verá o objetivo da etapa, seguido por uma célula vazia. Insira seu Python na célula e execute-o. A solução para cada etapa seguirá cada célula.

# Crie as variáveis
nome = 'Ganymede'
planeta = 'Marte'
gravidade = 1.43

mensagem = """ Fatos sobre a gravidade de {nome}
------------------------------
Nome do Planeta: {planeta}
Gravidade de {nome}: {gravidade} m/s2
"""

# Use o modelo
# Com o template criado, é hora de usá-lo para exibir informações sobre a lua! Use a função de formato no modelo para usar o modelo e imprimir as informações. Defina nome, planeta e gravidade para os valores apropriados.
print(mensagem.format(nome=nome, planeta=planeta, gravidade=gravidade))