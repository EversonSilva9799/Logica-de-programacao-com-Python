import time
from random import randrange
# Considerações: A lista numeros contém os números do cpf (quando este ainda está incompleto)

def CriaCpf():
  numeros = []
  mult_1 = 10
  mult_2 = 11
  while True:
    # Esta camada pode ser simplificada
    cpfParcial = input('Digite os nove primeiros dígitos do CPF: ')
    if len(cpfParcial) != 9:
      print('Digite nove números')
      time.sleep(2)
      CriaCpf()
    else:
      for j in cpfParcial:
        numeros.append(j)
      break
  #Recebe como argumento a lista com 9 dígitos (lista numeros)
  resto_1 = geraResto(numeros, mult_1)

  #Recebe o resto da função multiplicador e a lista ainda com 9 dígitos
  #OBS: adiciona o décimo número à lista
  comparaResto(resto_1, numeros)

  #Recebe como argumento a lista já com 10 dígitos
  resto_2 = geraResto(numeros, mult_2)

  #Recebe o resto da função multiplicador e a lista, agora com 10 dígitos
  comparaResto(resto_2, numeros)

  # Retorna a função responsável por agrupar a lista com o cpf
  # Esta função pode ser simplificada
  return(imprimiCpfGerado(numeros))

def consultaCpf(numeros):

  soma = 0
  mult_1 = 10
  mult_2 = 11

  resto_1 = geraResto(numeros, mult_1)
  comparaResto(resto_1, numeros)

  resto_2 = geraResto(numeros, mult_2)
  comparaResto(resto_2, numeros)
  numeros[9] = str(numeros[9])
  numeros[10] = str(numeros[10])

  return numeros


def geraCpfRandomico():
  """Função que gera cpf aleatório (não recebe nada como argumento"""

  #Função pode ser melhorada futuramente
  cpf = []
  numeros = []
  soma = 0
  mult_1 = 10
  mult_2 = 11
  for i in range(9):
    numeros.append(randrange(0, 10))

  resto_1 = geraResto(numeros, mult_1)
  comparaResto(resto_1, numeros)

  resto_2 = geraResto(numeros, mult_2)
  comparaResto(resto_2, numeros)

  return(imprimiCpfGerado(numeros))



def geraResto(numeros, mult):
  """ Esta função recebe a lista inicial dos números do cpf's e o multiplicador correspondente"""
  soma = 0
  mult_1 = 10
  mult_2 = 11
  for i in numeros:
     soma += int(i) * mult
     mult -= 1
  resto = soma%11
  return resto


def comparaResto(resto, numeros):
  """ Este método recebe o resto e compara com uma condição para descobrir os número verificadores do cpf"""
  restos = [2,3,4,5,6,7,8,9,10]
  if resto == 0 or resto == 1:
    numeros.append(0)
  elif resto in restos:
    numeros.append(11-resto)
  else:
    print('Erro! Tente novamente')

def imprimiCpfGerado(numeros):
  "Função responsável apenas por imprimir a lista com o cpf completo (recebe como argumento a lista do cpf)"""
  cpf = []
  for k in numeros:
    cpf.append(str(k))
  print('')
  print('')
  print('===========================')
  return "".join(cpf)
  print('===========================')
  del cpf[:]
  del numeros[:]
