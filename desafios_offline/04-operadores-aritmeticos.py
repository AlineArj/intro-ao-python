#Arithmetic operators in Python

# Python fornece operadores aritméticos comuns para que você possa realizar operações matemáticas em seu código. Estes incluem as quatro operações principais de adição, subtração, multiplicação e divisão.

# Vamos explorar como podemos criar um programa que pode calcular a distância entre dois planetas. Começaremos usando duas distâncias planetárias: Terra (149.597.870 km) e Júpiter (778.547.200 km).
terra = 149597870
jupiter = 778547200

# Exibir distância entre planetas
# Você tem duas variáveis que armazenam a distância entre cada planeta e um ponto comum - o sol. Você pode subtrair esses dois valores para determinar a distância entre os planetas.
distancia_km = jupiter - terra


# Em seguida, adicione o código para converter distance_km em milhas dividindo-o por 1,609 (a diferença aproximada entre milhas e quilômetros) e armazene o resultado em uma variável chamada distance_mi. Exiba o valor na tela.
distancia_mi = distancia_km / 1.609344

print(f"""A distância do planeta Terra até Júpiter
---------------------------------------
Em Km: {distancia_km} Km
Em Milhas: {distancia_mi} M""")
