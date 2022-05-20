# Analisar pedra, papel e tesoura para a modelagem OOP

# Descrição do problema: 
#   Pedra, papel e tesoura é um jogo com dois participantes. O jogo tem rodadas. Em cada rodada, um participante escolhe um símbolo de pedra, papel ou tesoura, e o outro participante faz o mesmo. O vencedor da rodada é determinado pela comparação dos símbolos escolhidos. As regras do jogo estabelecem que pedra ganha de tesoura, tesoura vence (corta) papel e papel vence (embrulha) pedra. O vencedor da rodada recebe um ponto. O jogo continua pela quantidade de rodadas que os participantes combinarem. O vencedor é o participante com o maior número de pontos.
class Participante:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.escolha = ''
        self.escolhas = {
            'pedra': 0,
            'papel': 1,
            'tesoura': 2,
            'largarto': 3,
            'spock': 4
        }
    def jogada(self):
        print()
        self.escolha = input(f'{self.nome}, escolha entre pedra, papel, tesoura, largarto ou spock: ')
        self.escolha = self.escolha.lower()

        if not self.escolha in self.escolhas:
            print('Opção inválida!')
            self.jogada()
        else:
            print(f'{self.nome} escolheu: {self.escolha}')

    def jogadaNum(self):
        return self.escolhas[self.escolha]
    def adicionaPontuacao(self):
        self.pontuacao += 1
    

class Rodada:
    def __init__(self, jogada1, jogada2):

        jogada1.jogada()
        jogada2.jogada()

        self.regras = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        resultado = self.comparaJogada(jogada1, jogada2)

        if resultado > 0:
            jogada1.adicionaPontuacao()
        elif resultado < 0:
            jogada2.adicionaPontuacao()
        else:
            print('\n------- EMPATE -------')
    def comparaJogada(self, jogada1, jogada2):
        return self.regras[jogada1.jogadaNum()][jogada2.jogadaNum()]


class Jogo:
    def __init__(self):
        self.fimJogo = False
        self.primeiroJogador = Participante(input('Digite o nome do jogador 1: '))
        self.segundoJogador = Participante(input('Digite o nome do jogador 2: '))
        self.contador = 1
    def iniciar(self):
        while not self.fimJogo:
            print('\n\n')
            print(f'########### PARTIDA {self.contador} ###########')
            Rodada(self.primeiroJogador, self.segundoJogador)
            self.fimJogo = self.finalizarJogo()
            self.contador += 1
    def finalizarJogo(self):
        print()
        resp = input('Iniciar nova partida? (s/n): ').lower()

        if resp == 's':
            return False
        elif resp == 'n':
            print()
            print('######### FIM DO JOGO #########')
            print(f'O jogador {self.primeiroJogador.nome} fez {self.primeiroJogador.pontuacao} pontos.')
            print(f'O jogador {self.segundoJogador.nome} fez {self.segundoJogador.pontuacao} pontos.')
            
            self.ganhador()
            return True
        else:
            print('Resposta inválida!') 
            self.finalizarJogo()  
    def ganhador(self):
        if self.primeiroJogador.pontuacao > self.segundoJogador.pontuacao:
            print()
            print(f'VITÓRIA PARA {self.primeiroJogador.nome}')
            print('-' * 30)

        elif self.primeiroJogador.pontuacao < self.segundoJogador.pontuacao:
            print()
            print(f'VITÓRIA PARA {self.segundoJogador.nome}')
            print('-' * 30)
        
        else:
            print()
            print(f'EMPATE')
            print('-' * 30)
        

jogo = Jogo()
jogo.iniciar()