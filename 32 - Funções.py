#Definição de uma função
def verificanumero(numero):
  if numero % 2 == 0:
    print('{} é par'.format(numero))
  else:
    print('{} é ímpar'.format(numero))

#Chamando a função
verificanumero(37)
verificanumero(74)

print('')
#Funções que retornam valores múltiplos
def potencia(numero):
  quadrado = numero ** 2
  cubo = numero ** 3
  return quadrado, cubo


quad, cub = potencia(5)

print("O quadrado é " , quad)
print("O cubo é " , cub)

  
