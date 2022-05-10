# Código referente ao desafio 10 no Mentimeter - apenas para referência, não é necessário
# fazer nada neste arquivo
import sys

def ler_argumentos():
    args = {}
    chave = ''
    for i, p in enumerate(sys.argv[1:]):
        if i % 2 == 0:
            chave = p
        else:
            args[chave] = p
    return args

def main():
    args = ler_argumentos()
    print(args)
main()
