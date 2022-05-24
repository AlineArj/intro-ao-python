import sys
import requests
import json
import csv
import string


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

def leitura_arq_json_lower():
    feiticos_dict_normal = leitura_arq_json()

    feiticos_dict_lower = {}
    for feitico in feiticos_dict_normal:
        feiticos_dict_lower[feitico.lower()] = feiticos_dict_normal[feitico]
    
    return feiticos_dict_lower

# Imprima para o usuário os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.
def pesquisa_feiticos():
    feitico_input = input('\nDigite um feitiço: ').lower()
    print()

    feiticos_dict = leitura_arq_json_lower()
    if feiticos_dict == -1:
        return False
    
    try:
        if feiticos_dict[feitico_input]:
            #print('#' * 6 + ' ' + capwords(feitico_input) + ' ' + '#' * 6)
            print(f'####### {string.capwords(feitico_input, sep = None)} #######')
            for chave, valor in feiticos_dict[feitico_input].items():
                print(f'- {chave}: {valor}')
            print('-' * 30)
    except KeyError:
        print('Feitiço não encontrado!')
    return True


# Nova pesquisa
def nova_pesquisa():
    resposta = input('\nRealizar nova pesquisa? (s/n): ').lower()

    if resposta == 'n':
        return False
    elif resposta == 's':
        return True
    else:
        print('Resposta inválida!')
        nova_pesquisa()



pesquisa = True
while pesquisa:
    pesquisa = pesquisa_feiticos()
    pesquisa = nova_pesquisa()


print('\n\nFim do Programa.')
