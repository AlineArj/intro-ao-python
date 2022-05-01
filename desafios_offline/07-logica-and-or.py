#Exercise: Use complex logic to determine possible evasive maneuvers

# No exercício anterior, você criou um código para testar o tamanho do objeto. Agora você testará o tamanho e a proximidade do objeto. Você usará o mesmo limite para o tamanho de 5m3. Se o objeto for maior que o limite e estiver a 1000 km do navio, serão necessárias manobras evasivas.

# Adicione o código à célula abaixo para criar duas variáveis: object_size e proximidade. Defina object_size como 10 para representar 10m3. Defina a proximidade para 9000.
from turtle import distance


tamanho_obj = 10
distancia = 9000

# Em seguida, adicione o código para exibir uma mensagem dizendo Manobras evasivas necessárias se o tamanho_do_objeto for maior que 5 e a proximidade for menor que 1000. Caso contrário, exiba uma mensagem dizendo que Objeto não representa ameaça.
if tamanho_obj > 5 and distancia < 1000:
    print('/!\ ALERTA /!\ - Necessária manobra evasiva')
else:
    print('Objeto não representa ameaça')
