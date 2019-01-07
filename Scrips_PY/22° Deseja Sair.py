listaNome = []
decisao = False
while True:
  if decisao == True:
    break
  listaNome.append(input('Digite seu nome: '))
  while True:
    sair = input('Deseja Sair? Sim/Não: ')
    if sair.lower() == 'sim':
      decisao = True
      break
    elif sair.lower() == 'não':
      break
    else:
      print('ESCOLHA SIM OU NÃO!')
      continue
print(listaNome)
