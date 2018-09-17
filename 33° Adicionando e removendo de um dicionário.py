listatel = {}

for i in range(5):
    nome = input('Nome: ')
    tel = input('Telefone: ')
    listatel[nome] = tel

print(listatel)

for i in range(2):
    remove = input('Nome: ')
    listatel.pop(remove)
    print(listatel)


# 'pop()' remove e retorna o elemento removido
# Por padrão 'pop()' remove o último elemento
# É possível especificar o elemento a ser removido pelo 'pop()'


    
