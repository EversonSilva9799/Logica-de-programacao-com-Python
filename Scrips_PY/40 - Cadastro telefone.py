listaTelefone = {}


def adicionaContato(nome, telefone):
  listaTelefone[nome] = telefone
  return('Cadastrado com sucesso')

def removeContato(nome):
  listaTelefone.pop(nome)
  return('Removido com sucesso')

def consultaTelefone(nome):
  if nome in listaTelefone:
    tel = listaTelefone[nome]
    return nome, tel
  return('Contato inexistente')

def exibiContatos():
  return(listaTelefone)






def menu():
  print('1 - Adicionar contatos à lista')
  print('2 - Remover contato')
  print('3 - Consultar lista')
  print('4 - Exibir todos os contatos')
  print('5 - Sair')
  print('')
  resposta = input('Selecionar: ')

  if resposta =='1':
    nome = input('Digite o nome: ')
    tel = input('Digite o telefone: ')
    resp = adicionaContato(nome, tel)
    print(resp)
    menu()

  elif resposta =='2':
    nome = input('Digite o nome: ')
    resp = removeContato(nome)
    print(resp)
    menu()

  elif resposta =='3':
    nome = input('Digite o nome: ')
    resp = consultaTelefone(nome)
    print(resp)
    menu()

  if resposta =='4':
    resp = exibiContatos()
    for contato, telefone in resp.items():
      print('-'*20)
      print('Nome: {}\nTelefone: {}'.format(contato, telefone))
      print('-'*20)
    menu()

'''
  if resposta =='5':
'''
menu()



