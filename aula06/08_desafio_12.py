# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. Escreva um arquivo de saída
# que contenha o conteúdo em JSON.
import csv
import json


caminho_csv = './exemplo2.csv'
with open(caminho_csv, 'r', encoding='utf-8') as arquivo_csv:
    conteudo_csv = csv.DictReader(arquivo_csv)
    conteudo_dict = {}
    for indice, conteudo in enumerate(conteudo_csv):
        conteudo_dict[indice + 1] = conteudo
        
caminho_json = './exemplo2_saida.json'
with open(caminho_json, 'w') as arquivo_json:
      json.dump(conteudo_dict, arquivo_json, ensure_ascii=False, indent=4)
