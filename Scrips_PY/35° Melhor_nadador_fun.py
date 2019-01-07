def pega_nome_nadador(dic, tempo):
    nome = "Não identificado"
    for chave, valor in dic.items():
        if valor == tempo:
           nome = chave
           return nome
    return nome
  
  
tempo_nadador = {}

for i in range(3):
  nome = input('Digite o nome do nadador: ')
  tempo = float(input('Digite o tempo do nadador: '))
  tempo_nadador[nome] = tempo

melhor_tempo = min(tempo_nadador.values())
pior_tempo = max(tempo_nadador.values())
best         = pega_nome_nadador(tempo_nadador, melhor_tempo)
worst        = pega_nome_nadador(tempo_nadador, pior_tempo)
print(best)
print(worst)