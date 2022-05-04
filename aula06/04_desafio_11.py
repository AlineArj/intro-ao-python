# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO
caminho01 = 'entrada_desafio_11.txt'
with open(caminho01, 'r') as arquivo01:
    text = arquivo01.read()

caminho02 = 'saida_desafio_11.txt'
with open(caminho02, 'w') as arquivo02:
    arquivo02.write(text[::-1])
