# Using while loops in Python

# Neste exercício, você está criando um aplicativo que solicita ao usuário que insira uma lista de planetas. Em um exercício posterior, você adicionará o código que exibe a lista. Por enquanto, porém, você criará apenas o código que avisa o usuário.

#Comece adicionando duas variáveis, uma para a entrada do usuário, chamada new_planet, e outra variável para a lista de planetas, chamada planetas.
novo_planeta = ''
planetas = []

# Começando com as variáveis que você acabou de criar, crie um loop while. O loop while será executado enquanto new_planet não estiver definido como concluído.
# Dentro do loop, verifique se a variável new_planet contém um valor, que deve ser o nome de um planeta. Essa é uma maneira rápida de ver se o usuário inseriu um valor. Se eles tiverem, seu código anexará esse valor à variável planets.
# Complete o loop while usando input para solicitar ao usuário que digite um novo nome de planeta ou use done se já tiver digitado nomes de planetas. Você armazenará o valor da entrada na variável new_planet.
print()
print("Adicione um planeta ou digite 'concluido' para finalizar o programa\n")

while novo_planeta.lower() != 'concluido':
    if novo_planeta:
        planetas.append(novo_planeta)

    novo_planeta = input('Novo planeta: ')

print()

# Crie um loop for para iterar sobre a lista de nomes de planetas. Você pode usar planet como o nome da variável para cada planeta. Dentro do loop for, use print para exibir o nome de cada planeta. imprimir declaração. Execute a célula e forneça uma lista de planetas.
print('Planetas adicionados: ')
for _ in planetas:
    print(_)
