from banco import *


class Fluxo:
    def __init__(self):
        self.contas = FluxoDeConta()
        self.iniciar()

    def menuPrincipal(self):
        print('MENU')
        print('(1) - Cadastro de Conta')
        print('(2) - Pesquisa de Titular')
        print('(3) - Operação em Conta')
        print('(4) - Finalizar')
        
    def opMenuPrincipal(self):
        resp_menu_principal = input('Digite: ')

        if resp_menu_principal == '1':
            self.contas.cadastrarConta()
        elif resp_menu_principal == '2':
            self.contas.pesquisarTitular()
        elif resp_menu_principal == '3':
            self.contas.opEmConta()
        elif resp_menu_principal == '4':
            print('Finalizando programa...')
            print()
            return False
        else:
            print('Resposta inválida, tente novamente!')
            self.opMenuPrincipal()
        return True

    def iniciar(self):
        resp = True
        while resp:
            self.menuPrincipal()
            resp = self.opMenuPrincipal()


iniciar = Fluxo()


