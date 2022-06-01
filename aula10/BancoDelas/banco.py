class Titular:
    def __init__(self, id_conta):
        self.__id_conta = id_conta
        self.dados_titular = {'Nome': '', 'Sexo': None, 'Telefone': '','Renda': 0, 'ID Conta': self.__id_conta}
        self.inputDadosTitular()

    def inputDadosTitular(self):
        while True:
            self._nome = input('Nome: ')

            if self._nome == '':
                print('ERRO: É necessário associar um nome ao cadastro.')
            else:
                break
        
        while True:
            self._sexo = input('Sexo (F / M / NB): ').upper()
            sexos = ['F', 'M', 'NB']
            
            if not self._sexo in sexos:
                print('Resposta inválida! Tente: (F) - Feminino, (M) - Masculino ou (NB) - Não Binário')
                continue
            else: break

        self.telefone = input('Telefone: ')
        self.renda = float(input('Renda: '))

        self.dados_titular['Nome'] = self._nome
        self.dados_titular['Telefone'] = self.telefone
        self.dados_titular['Sexo'] = self._sexo
        self.dados_titular['Renda'] = self.renda

        return self.dados_titular

    def mostrarDadosTitular(self):
        dados_str = f'\nDADOS DO TITULAR\n'
        dados_str += f'Nome: {self._nome}\n'
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
        self._saldo = int(input('Saldo: '))
        self.dados_conta['Saldo'] = self._saldo
        return self.dados_conta

    def __str__(self):
        self.saldo = self.dados_conta['Saldo']
        dados_str = '##CONTA##\n'
        dados_str += f'Saldo: {self.saldo}\n'
        return dados_str

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
        num_titulares = int(input('Num titulares: '))
        id_conta = len(self.__contas)
        cheque_especial = None

        for _ in range(num_titulares):
            dados_titular = Titular(id_conta)
            self._titulares.append(dados_titular)
            if cheque_especial == None:
                cheque_especial = self.checkChequeEspecial(dados_titular)

        self.__contas.append(Conta(id_conta, cheque_especial))
            
    def pesquisa(self):
        nome_pesquisa = input('Nome do Titular: ').lower()
        for titular in self._titulares:
            res_pesquisa = self.lendoDados(titular, nome_pesquisa)
            if res_pesquisa:
                break
        if res_pesquisa == None:
            print('Não encontrado!')
        
    def lendoDados(self, titular: Titular, nome_pesquisa):
        if titular._nome.lower() == nome_pesquisa:
            id_conta = titular.dados_titular['ID Conta']
            print(titular)
            print(self.__contas[id_conta])
            return True
        else:
            return None

    def opConta(self):
        nome_pesquisa = input('Nome do Titular: ').lower()
        for titular in self._titulares:
            conta_encontrada = self.opDados(titular, nome_pesquisa)
            if (conta_encontrada != None):
                verificadorConta(conta_encontrada)
                break
        if conta_encontrada == None:
            print('Não encontrado!')

    def opDados(self, titular: Titular, nome_pesquisa):
        if titular._nome.lower() == nome_pesquisa:
            id_conta = titular.dados_titular['ID Conta']
            print(titular._nome)
            return self.__contas[id_conta]
        else:
            return None
    
class opContaGeral:
    def __init__(self, conta: Conta):
        self.conta = conta
        self.saldo = conta.dados_conta['Saldo']
        self.iniciar()

    def menuOperacoes(self):
        print('OPERACOES')
        print('1 - Saque')
        print('2 - Deposito')
        print('3 - Sair')
    
    def deposito(self):
        deposito = float(input('Valor do depósito: '))
        if deposito > 0:
            self.saldo += deposito

            print(f'Saldo Atual: {self.saldo}')
        else:
            print('Valor inválido para deposito.')

    def saque(self):
        saque = float(input('Valor do saque: '))
        if saque <= self.saldo:
            self.saldo -= saque
            print(f'Saldo Atual: {self.saldo}')
        else:
            print('Saldo insuficiente')

    def  respostaOp(self):
        while True:
            resp_op_conta = input('Digite: ')
            if resp_op_conta == '1':
                self.deposito()
                return True
            elif resp_op_conta == '2':
                self.saque()
                return True
            elif resp_op_conta == '3':
                print('Saindo')
                return False
            else: 
                print('Resposa Inválida')

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
        print('OPERACOES')
        print('1 - Saque')
        print('2 - Deposito')
        print('3 - Consulta do Cheque especial')
        print('4 - Sair')

    def saque(self):
        saque = float(input('Valor do saque: '))
        x = (self.saldo >= saque)
        y = (self.saldo + self.cheque_esp >= saque)

        if x: 
            self.saldo -= saque
            print(f'Saldo Atual: {self.saldo}')
        elif y:
            valor_cheque_especial = self.saldo - saque
            self.cheque_esp += valor_cheque_especial
            self.saldo = valor_cheque_especial
            print(f'Saldo Atual: {self.saldo}')
        else:
            print('Saldo insuficiente')

    def saldoChequeEspecial(self):
        print(self.cheque_esp)

    def respostaOp(self):
        resp_op = input('Digite: ')

        if resp_op == '1':
            self.saque()
        elif resp_op == '2':
            self.deposito()
        elif resp_op == '3':
            self.saldoChequeEspecial()
        elif resp_op == '4':
            return False
        else:
            print('Resposta inválida, tente novamente!')
            self.respostaOp()
        return True

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
        self.banco = BancoDeContas()

    def respCadastro(self):
        while True:
            resp_cadastro = input('Realizar novo cadastro? (s/n): ').lower()

            if resp_cadastro == 's':
                return True
            elif resp_cadastro == 'n':
                return False
            else:
                print('Resposta inválida! Tente: (s) - Sim ou (n) - Não')
  
    def respPesquisa(self):
        while True:
            resp_pesquisa = input('Realizar nova pesquisa? (s/n): ').lower()

            if resp_pesquisa == 's':
                return True
            elif resp_pesquisa == 'n':
                return False
            else:
                print('Resposta inválida! Tente: (s) - Sim ou (n) - Não')

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


