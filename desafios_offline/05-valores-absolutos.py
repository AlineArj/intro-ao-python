# Crie um aplicativo para trabalhar com números e entrada do usuário

# Frequentemente, você precisará converter valores de string em números para executar corretamente diferentes operações ou determinar o valor absoluto de um número. Neste exercício, você criará um projeto para calcular a distância entre dois planetas com base na entrada do usuário.

# Comece adicionando o código para solicitar ao usuário a distância entre o sol e o primeiro planeta e depois o segundo. Armazene cada resultado em variáveis ​​denominadas first_planet_input e second_planet_input.
print('Insira a distância do sol até o planeta desejado em Km')
planeta01 = input('Primeiro planeta: ')
planeta02 = input('Segundo planeta: ')

planeta01 = int(planeta01)
planeta02 = int(planeta02)

# Faça o cálculo e converta para valor absoluto
# Com seus valores armazenados como números, agora você pode adicionar o código para realizar o cálculo, subtraindo o primeiro planeta do segundo. Como o segundo planeta pode ser um número maior, você usará abs para convertê-lo em um valor absoluto.
distancia_km = abs(planeta01 - planeta02)

print(f'A distância entre os planetas inseridos é de {distancia_km} Km')
