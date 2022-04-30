from datetime import datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
aniversario_str = input('\nDigite sey aniversário (dd/mm/aaaa): ')
aniversario_date = datetime.strptime(aniversario_str, '%d/%m/%Y').date()

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
hoje = datetime.now().date()
dias_aniversario = aniversario_date - hoje
print(f'\nFaltam {dias_aniversario.days} dias para seu aniversário!')

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
print()
pergunta_gosta = input('Você gosta do seu aniversário? (sim/nao): ')

pergunta_gosta = pergunta_gosta.lower()

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
pergunta_festa = input('Você fará festa de aniversário? (sim/nao): ')

pergunta_festa = pergunta_festa.lower()

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
print()
if pergunta_gosta and pergunta_festa == 'sim':
    print('VOCÊ VAI GANHAR PRESENTEEE!!')
else:
    print('Você não ganahará presentes esse ano.')
