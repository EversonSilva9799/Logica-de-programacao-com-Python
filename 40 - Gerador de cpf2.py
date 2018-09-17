from random import randint
numeros = []
cpf = []
soma = 0
mult_1 = 10
mult_2 = 11

quantidade = int(input('Quantos cpf deseja gerar? '))
for qt in range(quantidade):
    #Descobrindo o primeiro dígito verificador
    for i in range(9):
        numeros.append(randint(0,9))
    for j in numeros:
       soma = soma + int(j) * mult_1
       mult_1 = mult_1 - 1
    resto = soma%11
    
    soma = 0

    if resto == 0 or resto == 1:
      numeros.append(0)
    elif resto >= 2 or resto <=10: #resto == 3 or resto == 4 or resto == 5 or resto == 6 or resto == 7 or resto == 8 or resto == 9 or resto == 10:
      numeros.append(11-resto)
    

    #Descobrindo o segundo dígito verificador
    for n in numeros:
       soma = soma + int(n) * mult_2
       mult_2 = mult_2 - 1
    resto_2 = soma%11
    


    if resto_2 == 0 or resto_2 == 1:
      numeros.append(0)
    elif resto_2 >= 2 or resto_2 <=10: #or resto == 3 or resto == 4 or resto == 5 or resto == 6 or resto == 7 or resto == 8 or resto == 9 or resto == 10:
          numeros.append(11-resto_2)

    for k in numeros:
        cpf.append(str(k))
    print('')
    print('')
    print('===========================')
    print('O CPF é este')
    print(''.join(cpf))
    print('===========================')
    del numeros[:]
    del cpf[:]

