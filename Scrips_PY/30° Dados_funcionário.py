cadastro = {}


while True:
    
    nome = input('Digite o nome do funcionário: ')
    dados = []

    inf = input('Digite o fone do funcionário: ')    
    dados.append(inf)
    inf = input('Digite o sexo do funcionário: ')    
    dados.append(inf)
    inf = input('Digite o e-mail do funcionário: ')    
    dados.append(inf)
    inf = input('Digite o salário do funcionário: ')    
    dados.append(inf)
    cadastro[nome] = dados
    print('')
    print('')
    resposta = input('Continuar a cadastrar? sim/não: ')
    if resposta.lower() == "não":
        break

for chave,valor in cadastro.items():
    print('Funcionário: ',chave)
    for i in valor:
        print(i)
        


