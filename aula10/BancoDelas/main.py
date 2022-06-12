from banco import *
from colorama import init, Fore, Back, Style


class Fluxo:
    def __init__(self):
        self.contas = FluxoDeConta()
        self.iniciar()

    def menuPrincipal(self):
        print()
        print(Back.BLUE + Fore.WHITE + ' ########' + '  MENU  ' +  '######## ')
        print('(' + Fore.BLUE + '1' + Style.RESET_ALL + ') - Cadastro de Conta')
        print('(' + Fore.BLUE + '2' + Style.RESET_ALL + ') - Pesquisa de Titular')
        print('(' + Fore.BLUE + '3' + Style.RESET_ALL + ') - Operação em Conta')
        print('(' + Fore.BLUE + '4' + Style.RESET_ALL + ') - Finalizar')
        
    def opMenuPrincipal(self):
        print()
        resp_menu_principal = input(Style.BRIGHT + 'Digite: ' + Style.RESET_ALL)

        if resp_menu_principal == '1':
            self.contas.cadastrarConta()
        elif resp_menu_principal == '2':
            self.contas.pesquisarTitular()
        elif resp_menu_principal == '3':
            self.contas.opEmConta()
        elif resp_menu_principal == '4':
            print()
            print('Finalizando programa...')
            print()
            return False
        else:
            print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'Resposta inválida, tente novamente!')
            return self.opMenuPrincipal()
        return True

    def iniciar(self):
        resp = True
        while resp:
            self.menuPrincipal()
            resp = self.opMenuPrincipal()

init(autoreset=True)
iniciar = Fluxo()


