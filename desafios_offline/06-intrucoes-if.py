#Exercise: Use logic to examine an object's size

# Você iniciará seu projeto criando o código para determinar se um pedaço de lixo espacial é de tamanho perigoso. Para este exercício usaremos um tamanho arbitrário de 5 metros cúbicos (5m3); qualquer coisa maior é um objeto potencialmente perigoso.

# Na célula abaixo, adicione uma variável chamada object_size e defina-a como 10 para representar 10m3. Em seguida, adicione uma instrução if para testar se object_size for maior que 5. Se for, exiba uma mensagem dizendo Precisamos ficar de olho neste objeto. Se for menor que 5, exiba uma mensagem dizendo que Objeto não representa ameaça.
objeto = 10

if objeto >= 5:
    print('/!\ ALERTA /!\ - Objeto potencialmente perigoso')
else:
    print('Objeto não representa ameaça')