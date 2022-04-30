# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.
alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]

# Comece o programa perguntando o nome da aluna.
nome_pesquisa = input('Nome: ')
print('-' * 20)
print()

# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.
if nome_pesquisa in alunas:
    for indice, aluna in enumerate(alunas):
        if aluna == nome_pesquisa:
            print(f'Aluna: {aluna}')

            if notas[indice] < 60:
                print(f'Nota: \033[0;31m{notas[indice]}\033[m')
            elif notas[indice] > 90:
                print(f'Nota: \033[0;32m{notas[indice]}\033[m')
            else:
                print(f'Nota: {notas[indice]}')

else:
    print('\033[0;30;41m  ERRO: Nome não encontrado  \033[m')

print()
