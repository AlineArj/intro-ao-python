# Exercise: Create and modify a Python dictionary

# Os dicionários Python permitem modelar dados mais complexos. Dicionários são uma coleção de pares chave/valor e são muito comuns em programas Python. Sua flexibilidade permite trabalhar dinamicamente com valores relacionados sem precisar criar classes ou objetos.

# Você deseja criar um programa que armazene e exiba informações sobre planetas. Para começar, você usará um planeta. Crie uma variável chamada planeta. Armazene os seguintes valores como um dicionário: nome e luas.
planetas_rochosos = {
    'planeta_01': {
        'nome': 'Mercúrio',
        'luas': 0,
        'gravidade_m/s': 3.7,
        'raio_km': 2439.7
    },

    'planeta_02': {
        'nome': 'Vênus',
        'luas': 0,
        'gravidade_m/s': 8.87,
        'raio_km': 6051.8
    },

    'planeta_03': {
        'nome': 'Terra',
        'luas': 1,
        'gravidade_m/s': 9.80,
        'raio_km': 6371
    },

    'planeta_04': {
        'nome': 'Marte',
        'luas': 2,
        'gravidade_m/s': 3.72,
        'raio_km': 3389.5
    }
}

#  Exibir dados do planeta
# Com a variável criada, agora você exibirá as informações. Você pode recuperar informações usando get ou colchetes ([ ]) e o nome da chave. Adicione o código para exibir as informações do planeta no seguinte formato:
print(f"Os planetas rochosos do Sistema Solar são: {planetas_rochosos['planeta_01']['nome']}, {planetas_rochosos['planeta_02']['nome']}, {planetas_rochosos['planeta_03']['nome']} e {planetas_rochosos['planeta_04']['nome']}")
