import time

#Crie um decorator que calcule o tempo de execução de uma determinada função
def tempo_de_execucao(funcao):
    def wrapper():
        inicio = time.time()
        funcao()
        fim = time.time()
        
        print(f'Tempo de execução do programa: {fim - inicio:.2f} segundos')
    return wrapper


# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas
def encontrar_item(container, item):
    return item in container

@tempo_de_execucao
def main():
    tamanho = 1000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item)
    encontrar_item(lista_grande, item)

if __name__ == '__main__':
    main()
