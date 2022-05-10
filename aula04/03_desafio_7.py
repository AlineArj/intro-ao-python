## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?
import colorama


def calcular_media(valores):
    tamanho = len(valores)
    soma = 0.0
    for i, valor in enumerate(valores):
        soma += valor
        i += 1
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    
    if valor.lower() == 'ok':
        continuar = False
    else: 
        try:
            valores.append(float(valor))  
        except ValueError:
            print (colorama.Fore.RED + "ERRO: " + colorama.Style.RESET_ALL + f"O valor '{valor}' é inválido!")

media_calculada = calcular_media(valores)
print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media_calculada))
