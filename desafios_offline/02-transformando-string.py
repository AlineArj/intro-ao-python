# Exercise: Transform strings

# Existem várias operações que você pode realizar em strings ao manipulá-las. Neste exercício, você usará métodos de string para modificar o texto com fatos sobre a Lua e, em seguida, extrair informações para criar um breve resumo.
# Este exercício é dividido em uma série de etapas. Para cada etapa, você verá o objetivo da etapa, seguido por uma célula vazia. Insira seu Python na célula e execute-o. A solução para cada etapa seguirá cada célula.

# Analisando fatos interessantes sobre a lua:
# " Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C. "

texto_lua = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

texto = texto_lua.lower()
# Separe o parágrafo em frases
# Em inglês, cada frase termina com um ponto. Você usará isso para quebrar o parágrafo em frases de diferença. Usando o método split para dividir o texto em frases procurando a string . (um ponto seguido de um espaço). Armazene o resultado em uma variável chamada frases. Imprima o resultado.
frases = texto.split('. ')

# Encontrar palavras-chave
# Você terminará seu programa adicionando o código para encontrar quaisquer frases que mencionem temperatura. Adicione código para percorrer a variável de sentenças. Para cada frase, procure a palavra temperatura. Se a palavra for encontrada, imprima a frase.
palavra = 'moon'

for frase in frases:
    if palavra in frase:
        print(frase)

