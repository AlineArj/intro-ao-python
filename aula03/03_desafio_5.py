# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).
lista = list(range(1, 61))

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
print(f'Índice | Item')
for i, num in enumerate(lista):
    if num % 2 == 0:
        print(f' {i} | {num}')