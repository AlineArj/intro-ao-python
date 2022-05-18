# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self):
        self.ligada = False
        self.velocidade = 0
        self.velocidade_max = 350
        self.cor = 'Vermelha'
        self.modelo = '1234M'
    
    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        if self.velocidade == 0:
            self.ligada = False
        else:
            print(f'Desacelere antes de desligar o carro!')
            return
    
    def acelerar(self):
        if self.ligada:
            if self.velocidade < self.velocidade_max:
                self.velocidade += 30
        else:
            return

    def desacelerar(self):
        if self.ligada:
            if 10 <= self.velocidade:
                self.velocidade -= 10
            # Utilizando o elif para garantir que a velocidade nunca seja negativa
            elif self.velocidade < 10:
                self.velocidade = 0
        else:
            return
    
    def __str__(self) -> str:
        return f'''STATUS DO CARRO: Ligado: {self.ligada}
                 Velocidade (Km/h): {self.velocidade}
                 Modelo: {self.modelo}
                 Cor: {self.cor}'''

# Crie uma instância da classe carro.
meu_carro = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
meu_carro.ligar()
meu_carro.acelerar()
print(meu_carro)

for _ in range(5):
    meu_carro.acelerar()

print(meu_carro)

# Faça o carro "parar" utilizando os métodos da sua classe.
for _ in range(18):
    meu_carro.desacelerar()

meu_carro.desligar()
print(meu_carro)