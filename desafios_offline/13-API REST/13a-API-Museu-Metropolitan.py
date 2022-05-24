import requests
import json

# Retorna uma lista de todos os IDs de objeto para objetos que contêm a consulta de pesquisa nos dados do objeto
q = ""
# Retorna objetos que correspondem à consulta, pesquisando especificamente o nome do artista ou o campo de cultura para objetos.
artistOrCulture = True
# Retorna objetos que correspondem à consulta, pesquisando especificamente no campo de título para objetos.
title = True
# Quando "true" indica uma obra de arte popular e importante na coleção
isHighlight = True
# Departamento da arte (int) 6 -> Asiatico / 21 -> Moderna / 19 -> Fotografia
departmentId = 9
# Retorna objetos que correspondem à consulta e estão em exibição no museu.
isOnView = True
# Retorna objetos que correspondem à consulta e possuem imagens.
hasImages = True
# Retorna objetos que correspondem à consulta e à localização geográfica especificada. Os exemplos incluem: "Europa", "França", "Paris", "China", "Nova York", etc.
geoLocation = ""

parametros = {'q': q, 'departmentId': departmentId, 'isHighlight': isHighlight, 'hasImages': hasImages, 'isOnView': isOnView}

# Filtrando as obras de arte
URL_pesquisa = "https://collectionapi.metmuseum.org/public/collection/v1/search"
resposta = requests.get(URL_pesquisa, parametros)
conteudo = json.loads(resposta.text)
print(conteudo)

print('\n\n')

# Percorrendo os IDs e mostrando dados das  obras
for id in conteudo['objectIDs']:
    URL_obra = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(id)
    resposta_obra = requests.get(URL_obra)
    conteudo_obra = json.loads(resposta_obra.text)

    # Conteudo
    artista = conteudo_obra["artistDisplayName"]
    vida_artista = conteudo_obra["artistDisplayBio"]
    nome_obra = conteudo_obra["title"]
    imagem_obra = conteudo_obra["additionalImages"]
    data_criacao = conteudo_obra["objectDate"]
    materiais = conteudo_obra["medium"]
    dimensoes = conteudo_obra["dimensions"]
    wiki_obra = conteudo_obra["objectWikidata_URL"]

    
    print(f'Nome do artista: {artista}\nVida do artista: {vida_artista}\nNome da Obra: {nome_obra}\nImagem: {imagem_obra}\nData de criação: {data_criacao}\nMateriais: {materiais}\nDimensões: {dimensoes}\nSaiba mais: {wiki_obra}\n\n')

