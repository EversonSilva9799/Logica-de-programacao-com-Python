class Carro():
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        self.velocidade = velocidade
        

    def abastecer(self, qtd):
        self.qtd_combustivel += qtd

    def ligar(self):
        if self.is_ligado:
            print("O carro já está ligado")
        else:
            self.is_ligado = True
            print("O carro foi ligado")

    def desligar(self):
        if self.is_ligado == False:
            print("O carro já está desligado")
        else:
            self.is_ligado = False
            print("O carro foi desligado")

    def acelerar(self, velocidade):
        if self.is_ligado:
            self.velocidade = velocidade
        else:
            print("Não foi possível acelerar"   )


    



        
