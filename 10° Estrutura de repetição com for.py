#Estrutura de repetição

# Faz quase o mesmo que o "while"
# lê-se assim:  "para" valor    "até" outro valor "começando de"
#                for variável     in   variável        range


#exemplo:
'''
for cont in range(comece de -valor- , até -valor- )
    print(cont)
'''

# Parâmetros do range (inicialização,até onde ir,de quanto em quanto)

n= 150000
cont = 0

for cont in range(0,n,5):
    print(cont)
