#from Carro import *
import carro

uno_vermelho = carro.Carro("Vermelho", 4, "Flex", 1.0, 0, False, 0)

uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(8)
uno_vermelho.acelerar(20)


print(uno_vermelho.is_ligado)
print("Quantidade de combustível: ",uno_vermelho.qtd_combustivel)
print(uno_vermelho.velocidade)






