total = 0
resto = 0
resto2 = 0
valor_fixo = 7



consumo = int(input("Digite o consumo de água: "))
if consumo == 0 and consumo <= 10:
    print(7)
elif consumo > 10 and consumo <= 30:
    resto = consumo - 10
    total = resto*1
    print(total+valor_fixo)
elif consumo > 30 and consumo <= 100:
    resto = consumo - 10
    resto2 = resto-20
    total = resto2*2
    print(total+valor_fixo+20*1)
elif consumo > 101:
    resto = consumo-10
    resto2 = resto-20
    resto3 = resto2-70
    total = resto3*5
    print(total+valor_fixo+20*1+70*2)
    
               
                 
              
              
            
