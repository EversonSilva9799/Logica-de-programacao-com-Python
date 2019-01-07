def pesquisaLista(lista, valor):
    for i, valores in enumerate(lista):
        if valor == valores:
            return('O elemento {} está no índice {}'.format(valor, i))
    return('Não existe na lista')


lista = [5, "Everson", 6, 65, "Alcides", "Lurdinha"]

print('1 - Número\n2 - Caractere')
resposta = input('Deseja pesquisar um número ou caracteres? ')

if resposta == '1':
    valor = int(input('Pesquisar: '))
    resp = pesquisaLista(lista, valor)
    print(resp)
else:
    valor = input('Pesquisar: ')
    pesquisaLista(lista, valor)
    resp = pesquisaLista(lista, valor)
    print(resp)
                      
    
