import sys
import requests
import json
import csv


# Crie uma aplicação que lê na linha de comando o nome de um feitiço
# Utilize a biblioteca requests para ler o JSON disponível em https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
def leitura_arq_json():
    URL_feiticos_json = "https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json"

    try:
        resultado_json = requests.get(URL_feiticos_json)
    except:
        print('Os dados dos feitiços estão indisponíveis no momento!\n')
        return -1
    else:
        feiticos_json = resultado_json.text
        feiticos_dict = json.loads(feiticos_json)
        return feiticos_dict


# Imprima para o usuário os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.
def pesquisa_feiticos():
    feitico_input = input('Digite um feitiço: ')
    print()

    feiticos_dict = leitura_arq_json()

    if feiticos_dict == -1:
        return False
    
    try:
        if feiticos_dict[feitico_input]:
            print('#' * 6 + ' ' + feitico_input + ' ' + '#' * 6)
            print()
            for chave, valor in feiticos_dict[feitico_input].items():
                print(f'- {chave}: {valor}')
            print('-' * 30)
    except KeyError:
        print('Feitiço não encontrado!')
    return True


# Nova pesquisa
def nova_pesquisa():
    resposta = input('\nRealizar nova pesquisa? (s/n): ')

    if resposta.lower() == 'n':
        return False
    elif resposta.lower() == 's':
        return True
    else:
        print('Resposta inválida!')
        nova_pesquisa()



pesquisa = True
while pesquisa:
    pesquisa = pesquisa_feiticos()
    pesquisa = nova_pesquisa()


print('\n\nFim do Programa.')
