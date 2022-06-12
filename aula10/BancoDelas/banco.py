from colorama import init, Fore, Back, Style

class Titular:
    def __init__(self, id_conta):
        self.__id_conta = id_conta
        self.dados_titular = {'Nome': '', 'Sexo': None, 'Telefone': '','Renda': 0, 'ID Conta': self.__id_conta}
        self.inputDadosTitular()

    def inputDadosTitular(self):
        print()
        while True:
            self._nome = input(Style.BRIGHT + 'Nome: ' + Style.RESET_ALL)

            if self._nome == '':
                print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'É necessário associar um nome ao cadastro.')
            else: break
        
        while True:
            self._sexo = input(Style.BRIGHT + 'Gênero (F / M / NB): ' + Style.RESET_ALL).upper()
            sexos = ['F', 'M', 'NB']
            
            if not self._sexo in sexos:
                print(Fore.RED + 'ERRO:' + Style.RESET_ALL + ' Resposta inválida! Tente: F - Feminino, M - Masculino ou NB - Não Binário.')
                continue
            else: break

        self.telefone = input(Style.BRIGHT + 'Telefone: ' + Style.RESET_ALL)
        self.renda = float(input(Style.BRIGHT + 'Renda: ' + Style.RESET_ALL))

        self.dados_titular['Nome'] = self._nome
        self.dados_titular['Telefone'] = self.telefone
        self.dados_titular['Sexo'] = self._sexo
        self.dados_titular['Renda'] = self.renda

        return self.dados_titular

    def mostrarDadosTitular(self):
        print (Fore.BLUE + '\nDADOS DO TITULAR')
        dados_str = f'Nome: {self._nome.capitalize()}\n'
        dados_str += f'Telefone: {self.telefone}\n'
        return dados_str

    def __str__(self):
        return self.mostrarDadosTitular()
    
class Conta:
    def __init__(self, id_conta, cheque_especial):
        self.cheque_especial = cheque_especial
        self.dados_conta = {'ID Conta': id_conta, 'Saldo': 0, 'Cheque Especial': self.cheque_especial}
        self.inputDadosConta()

    def inputDadosConta(self):
        print()
        self._saldo = float(input(Style.BRIGHT + 'Saldo: ' + Style.RESET_ALL))
        self.dados_conta['Saldo'] = self._saldo
        return self.dados_conta
    
    def mostrarDadosConta(self):
        self.saldo = self.dados_conta['Saldo']
        print('------' + Style.BRIGHT + ' CONTA ' + Style.RESET_ALL + '------')
        dados_str = f'Saldo: {self.saldo}\n'
        
        dados_str += f'- Cheque Especial -\n'
        dados_str += f'Status: '
        if self.cheque_especial == None:
            dados_str += f'Indisponível\n'
        else:
            dados_str += f'Disponível\n'
            dados_str += f'Saldo: R$ {self.cheque_especial}'
        return dados_str

    def __str__(self):
        return self.mostrarDadosConta()

class BancoDeContas:
    def __init__(self):
        self._titulares = []
        self.__contas = []

    def checkChequeEspecial(self, titular: Titular):
        if titular._sexo == 'F':
            return titular.renda
        else:
            return None

    def cadastro(self):
        print()
        num_titulares = int(input('Número de titulares: '))

        if num_titulares <= 0:
            print(Fore.RED + 'ERRO:' + Style.RESET_ALL + ' Número de titulares inválido!')
        else:
            id_conta = len(self.__contas)
            cheque_especial = None

            for _ in range(num_titulares):
                dados_titular = Titular(id_conta)
                self._titulares.append(dados_titular)
                if cheque_especial == None:
                    cheque_especial = self.checkChequeEspecial(dados_titular)
            self.__contas.append(Conta(id_conta, cheque_especial))
            
    def pesquisa(self):
        print()
        nome_pesquisa = input('Pesquisar titular: ').lower()
        for titular in self._titulares:
            res_pesquisa = self.lendoDados(titular, nome_pesquisa)
            if res_pesquisa:
                break
        if res_pesquisa == None:
            print(Fore.RED + 'Não encontrado!')
        
    def lendoDados(self, titular: Titular, nome_pesquisa):
        if titular._nome.lower() == nome_pesquisa:
            id_conta = titular.dados_titular['ID Conta']
            print(titular)
            print(self.__contas[id_conta])
            return True
        else:
            return None

    def opConta(self):
        print()
        nome_pesquisa = input('Nome do Titular: ').lower()
        for titular in self._titulares:
            conta_encontrada = self.opDados(titular, nome_pesquisa)
            if (conta_encontrada != None):
                verificadorConta(conta_encontrada)
                break
        if conta_encontrada == None:
            print(Fore.RED + 'Não encontrado!')

    def opDados(self, titular: Titular, nome_pesquisa):
        if titular._nome.lower() == nome_pesquisa:
            id_conta = titular.dados_titular['ID Conta']
            return self.__contas[id_conta]
        else:
            return None
    
class opContaGeral:
    def __init__(self, conta: Conta):
        self.conta = conta
        self.saldo = conta.dados_conta['Saldo']
        self.iniciar()

    def menuOperacoes(self):
        print()
        print(Back.BLUE + f'*** OPERAÇÕES ***')
        print(Fore.BLUE + '1' + Style.RESET_ALL + ' - Saque')
        print(Fore.BLUE + '2' + Style.RESET_ALL + ' - Deposito')
        print(Fore.BLUE + '3' + Style.RESET_ALL + ' - Sair')
    
    def deposito(self):
        print()
        deposito = float(input('Valor do Depósito: R$ '))
        if deposito > 0:
            self.saldo += deposito
            self.mostraSaldo()
        else:
            print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'Valor inválido para deposito.')

    def saque(self):
        print()
        saque = float(input('Valor do Saque: R$ '))
        if saque <= self.saldo and saque > 0:
            self.saldo -= saque
        else:
            print(Fore.RED + 'Saldo Insuficiente!')
        self.mostraSaldo()

    def mostraSaldo(self):
        if self.saldo > 0:
                print('Saldo Atual: R$ ' + Fore.GREEN + f'{self.saldo}')
        else:
            print('Saldo Atual: R$ ' + Fore.RED + f'{self.saldo}')

    def  respostaOp(self):
        print()
        while True:
            resp_op_conta = input(Style.BRIGHT + 'Digite: ' + Style.RESET_ALL)
            if resp_op_conta == '1':
                self.saque()
                return True
            elif resp_op_conta == '2':
                self.deposito()
                return True
            elif resp_op_conta == '3':
                print(Fore.LIGHTGREEN_EX + '  Operação em conta finalizada  ' + Style.RESET_ALL)
                return False
            else: 
                print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'Resposta inválida, tente novamente!')

    def atualizaValores(self):
        self.conta.dados_conta['Saldo'] = self.saldo
    
    def iniciar(self):
        resp = True
        while resp:
            self.menuOperacoes()
            self.atualizaValores()
            resp = self.respostaOp()

class opContaFem(opContaGeral):
    def __init__(self, conta: Conta):
        self.conta = conta
        self.saldo = conta.dados_conta['Saldo']
        self.cheque_esp = conta.dados_conta['Cheque Especial']
        self.iniciar()

    def menuOperacoes(self):
        print()
        print(Back.BLUE + f'*** OPERAÇÕES ***')
        print(Fore.BLUE + '1' + Style.RESET_ALL + ' - Saque')
        print(Fore.BLUE + '2' + Style.RESET_ALL + ' - Deposito')
        print(Fore.BLUE + '3' + Style.RESET_ALL + ' - Consulta do Cheque especial')
        print(Fore.BLUE + '4' + Style.RESET_ALL + ' - Sair')

    def saque(self):
        print()
        saque = float(input('Valor do Saque: R$ '))
        
        x = (self.saldo >= saque)
        y = (self.saldo + self.cheque_esp >= saque)
        z = (saque > 0)

        if x and z: 
            self.saldo -= saque
        elif y and z:
            if self.saldo > 0:
                valor_cheque_especial = self.saldo - saque
                self.cheque_esp += valor_cheque_especial
                self.saldo = valor_cheque_especial
            else:
                self.cheque_esp -= saque
                self.saldo = self.saldo - saque
        else:
            print(Fore.RED + 'Saldo Insuficiente!')
        
        self.mostraSaldo()

    def deposito(self):
        print()
        deposito = float(input('Valor do Depósito: R$ '))
        if deposito > 0:
            if self.saldo > 0:
                self.saldo += deposito
            else:
                # Corrigir logica
                valor_cheque_especial = self.saldo + deposito
                self.saldo += deposito
                self.cheque_esp += valor_cheque_especial
            self.mostraSaldo()
        else:
            print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'Valor inválido para deposito.')
    
    def saldoChequeEspecial(self):
        print(f'\nSaldo Cheque Especial - R$ {self.cheque_esp}')

    def respostaOp(self):
        print()
        while True:
            resp_op = input(Style.BRIGHT + 'Digite: ' + Style.RESET_ALL)
            if resp_op == '1':
                self.saque()
                return True
            elif resp_op == '2':
                self.deposito()
                return True
            elif resp_op == '3':
                self.saldoChequeEspecial()
                return True
            elif resp_op == '4':
                print(Fore.LIGHTGREEN_EX + '  Operação em conta finalizada  ' + Style.RESET_ALL)
                return False
            else:
                print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'Resposta inválida, tente novamente!')

    def atualizaValores(self):
        self.conta.dados_conta['Saldo'] = self.saldo
        self.conta.dados_conta['Cheque Especial'] = self.cheque_esp

    def iniciar(self):
        resp = True
        while resp:
            self.menuOperacoes()
            self.atualizaValores()
            resp = self.respostaOp()
            

def verificadorConta(conta_encontrada: Conta):
    print(conta_encontrada)
    cheque_especial = conta_encontrada.dados_conta['Cheque Especial']
    if cheque_especial == None:
        opContaGeral(conta_encontrada)
    else:
        opContaFem(conta_encontrada)

class FluxoDeConta():
    def __init__(self):
        init(autoreset=True)
        self.banco = BancoDeContas()

    def respCadastro(self):
        while True:
            print()
            resp_cadastro = input('Realizar novo cadastro? (s/n): ').lower()

            if resp_cadastro == 's':
                return True
            elif resp_cadastro == 'n':
                return False
            else:
                print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'Resposta inválida! Tente: s - Sim ou n - Não')
  
    def respPesquisa(self):
        while True:
            print()
            resp_pesquisa = input('Realizar nova pesquisa? (s/n): ').lower()

            if resp_pesquisa == 's':
                return True
            elif resp_pesquisa == 'n':
                return False
            else:
                print(Fore.RED + 'ERRO:' + Style.RESET_ALL + 'Resposta inválida! Tente: s - Sim ou n - Não')

    def cadastrarConta(self):
        continua = True
        while continua:
            self.banco.cadastro()
            continua = self.respCadastro()

    def pesquisarTitular(self):
        continua = True
        while continua:
            self.banco.pesquisa()
            continua = self.respPesquisa()
    
    def opEmConta(self):
        self.banco.opConta()


