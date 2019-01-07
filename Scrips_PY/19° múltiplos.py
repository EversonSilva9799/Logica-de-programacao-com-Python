resposta = int(input("20 primeiros múltiplos de: "))
for i in range(1, 21):
  multiplo = resposta*i
  print("O {}° é ({}) ".format(i, multiplo))
