import random
letras = ['a','b','c','d','e']
gabarito = []
acertos_publica = 0
acertos_privada = 0
apv_publica = 0
apv_privada = 0
for i in range(5):
  gab = random.choice(letras)
  gabarito.append(gab)
print('Gabarito',gabarito)
volta = 0
while True:
    print('Aluno da rede pública(1), particular(2)')
    ensino = int(input("Sou da: "))
    print('')
    if ensino == 1:
        for j in range(1,6):
            resposta = input('Resposta da questão {}: '.format(j))
            if resposta.lower() == gabarito[j-1]:
                acertos_publica += 1
                apv_publica += (acertos_publica/5+volta)*100
                volta += 5
            acertos_publica = 0
        print(apv_publica)
                
        
    else:
        for j in range(1,6):
            resposta = input('Resposta da questão {}: '.format(j))
            if resposta.lower() == gabarito[j-1]:
                acertos_privada +=  1
                apv_privada += (acertos_privada/5+volta)*100
                volta += 5
            acertos_privada = 0
        print(apv_privada)
                
        
