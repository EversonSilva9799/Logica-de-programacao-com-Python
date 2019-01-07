import time, os
def cadastrar_usuario(mat, nome):
  alunos[mat] = nome
  return('Cadastro Realizado com sucesso!')

def remover_usuario(mat):
  if mat in alunos:
     alunos.pop(mat)
     return 'Aluno removido.'
  else:
     return('Aluno não cadastrado!')
  

def consultar_alunos(mat):
  if mat in alunos:
    return(alunos[mat])
  else:
    return('Aluno não cadastrado!')

def gerar_relatorio():
  return alunos

alunos = {}
def menu():
    print('-'*15)
    print('1 - Cadastrar aluno')
    print('2 - Romover aluno')
    print('3 - Consultar')
    print('4 - Gerar um relatório')
    print('0 - Sair')
    print('-'*15)
    resp = input('Selecionar: ')
    
    print('')

    if resp =='1':
      mat = int(input("Digite a matrícula: "))
      nome = input('Digite o nome: ')
      resp = cadastrar_usuario(mat, nome)
      print(resp)
      time.sleep(2)
      voltar = input('Digite enter para retornar ao menu!')
      if len(voltar) == 0:
          menu()
      else:
        print('Programa finalizado')

    elif resp == '2':
      mat = int(input("Digite a matrícula: "))
      resp = remover_usuario(mat)
      print(resp)
      time.sleep(2)
      voltar = input('Digite enter para retornar ao menu!')
      if len(voltar) == 0:
          menu()
      else:
        print('Programa finalizado')
      
    elif resp == '3':
      mat = int(input("Digite a matrícula: "))
      print("Dados do aluno: \n",consultar_alunos(mat))
      time.sleep(2)
      voltar = input('Digite enter para retornar ao menu!')
      if len(voltar) == 0:
          menu()
      else:
        print('Programa finalizado')
      
    elif resp == '4':
      resp = gerar_relatorio()
      for chave, valor in resp.items():
          print('-'*25)
          print('Matrícula:{}\nAluno:{}'.format(chave, valor))
          print('-'*25)
          
      voltar = input('Digite enter para retornar ao menu!')
      if len(voltar) == 0:
          menu()
      else:
        print('Programa finalizado')
     
    elif resp == '0':
        print('Programa finalizado')
        
    else:
        print('ESCOLHA UMA DAS OPÇÕES DO MENU')
        menu()

menu()



