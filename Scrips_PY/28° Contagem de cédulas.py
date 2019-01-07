valor = 0
notas = [100,50,20,10,5,2,1]
valor_total = []
valor = 0
print('CONTAGEM DE CÉDULAS')
while True:
    valor = int(input('Digite o total de dinheiro inteiro: '))
    if type(valor) != type(int(1)):
        print('Digite um valor inteiro')
        continue
    for i in notas:
        if i <= valor:
            valor = valor + valor//i
            valor = valor - valor*i
            valor_total.append(valor)
            print('{} nota(s) de {}'.format(valor, i))
            valor = 0
            if valor == 0:
                break














